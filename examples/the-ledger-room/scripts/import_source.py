#!/usr/bin/env python3
"""Preserve a source and extract traceable reading text. Never overwrites a manuscript."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import uuid
import xml.etree.ElementTree as ET
import zipfile

MAX_SOURCE = 50 * 1024 * 1024
MAX_TEXT = 20 * 1024 * 1024
FORMATS = {'.fdx': 'fdx', '.fountain': 'text', '.txt': 'text', '.md': 'text', '.docx': 'docx', '.pdf': 'pdf'}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def xml_root(data):
    if b'\x00' in data:
        raise ValueError('Save XML sources as UTF-8 before importing; UTF-16 and binary XML are not supported.')
    if re.search(br'<!\s*(DOCTYPE|ENTITY)\b', data, re.I):
        raise ValueError('XML declarations with DOCTYPE or entities are not supported. Export a plain-text copy instead.')
    try:
        return ET.fromstring(data)
    except ET.ParseError as exc:
        raise ValueError('The source contains unreadable XML; export a fresh copy.') from exc


def extract(data, fmt, original):
    warnings = []
    if fmt == 'text':
        try:
            text = data.decode('utf-8-sig')
        except UnicodeDecodeError as exc:
            raise ValueError('Save this text file as UTF-8, then import it again.') from exc
        if '\x00' in text:
            raise ValueError('This does not appear to be a text file.')
        segments = [{'location': f'line {number}', 'text': line} for number, line in enumerate(text.splitlines(), 1)]
    elif fmt == 'fdx':
        tree = xml_root(data)
        if tree.tag.split('}')[-1] != 'FinalDraft':
            raise ValueError('This file is not a Final Draft XML screenplay.')
        content = next((item for item in tree if item.tag.split('}')[-1] == 'Content'), None)
        if content is None:
            raise ValueError('The Final Draft file has no screenplay Content section.')
        segments = []
        for paragraph in content.iter():
            if paragraph.tag.split('}')[-1] != 'Paragraph':
                continue
            text = ''.join(''.join(item.itertext()) for item in paragraph if item.tag.split('}')[-1] == 'Text')
            segments.append({'location': f'paragraph {len(segments) + 1}', 'type': paragraph.get('Type', 'unspecified'), 'text': text})
        warnings.append('Final Draft paragraph types are retained; page layout, revisions, dual dialogue, notes, and embedded media are not reproduced.')
    elif fmt == 'docx':
        import io
        try:
            with zipfile.ZipFile(io.BytesIO(data)) as archive:
                entries = archive.infolist()
                if len(entries) > 2000 or sum(item.file_size for item in entries) > MAX_SOURCE:
                    raise ValueError('This Word archive is too large to extract safely.')
                matches = [item for item in entries if item.filename == 'word/document.xml']
                if len(matches) != 1 or matches[0].file_size > MAX_TEXT or matches[0].flag_bits & 1:
                    raise ValueError('This Word file has no single readable document body.')
                tree = xml_root(archive.read(matches[0]))
        except (zipfile.BadZipFile, RuntimeError) as exc:
            raise ValueError('The Word file could not be opened; save an unencrypted DOCX copy.') from exc
        ns = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
        segments = []
        for paragraph in tree.iter(ns + 'p'):
            parts = []
            for item in paragraph.iter():
                if item.tag == ns + 't': parts.append(item.text or '')
                elif item.tag == ns + 'tab': parts.append('\t')
                elif item.tag in (ns + 'br', ns + 'cr'): parts.append('\n')
            segments.append({'location': f'body paragraph {len(segments) + 1}', 'text': ''.join(parts)})
        warnings.append('Word body paragraphs and table-cell text are extracted in document order. Headers, footnotes, comments, text boxes, tracked-change meaning, images, and page layout are not verified; supply these separately when material.')
    elif fmt == 'pdf':
        program = shutil.which('pdftotext')
        if not program:
            raise ValueError('PDF extraction needs pdftotext (Poppler). Supply a text/Fountain/FDX/DOCX copy or ask your assistant for installation help. No OCR was attempted.')
        with tempfile.TemporaryDirectory(prefix='story-read-') as folder:
            # Read the exact bytes captured for the import, never a changing original.
            source = Path(folder) / 'source.pdf'
            target = Path(folder) / 'extracted.txt'
            source.write_bytes(data)
            try:
                result = subprocess.run([program, '-layout', '-enc', 'UTF-8', str(source), str(target)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=60)
            except subprocess.TimeoutExpired as exc:
                raise ValueError('PDF extraction timed out. Try a smaller, unencrypted text export.') from exc
            if result.returncode or not target.is_file():
                raise ValueError('PDF text could not be read. Export an unencrypted readable copy; no OCR was attempted.')
            if target.stat().st_size > MAX_TEXT:
                raise ValueError('Extracted PDF text exceeds the safe reading limit.')
            text = target.read_text(encoding='utf-8')
        pages = text.split('\f')
        if pages and not pages[-1].strip(): pages.pop()
        segments = [{'location': f'PDF page {i}', 'text': page.rstrip()} for i, page in enumerate(pages, 1)]
        empty = [item['location'] for item in segments if not item['text'].strip()]
        if empty:
            warnings.append('Pages without extracted text: ' + ', '.join(empty) + '. They may contain images, scans, or intentional blanks. Inspect the PDF before claiming a complete reading.')
        warnings.append('PDF page locations refer to file pages, not printed page labels. Reading order and visual formatting need comparison with the original. No OCR was performed.')
    else:
        raise ValueError('Unsupported source format.')
    if sum(len(item['text'].encode('utf-8')) for item in segments) > MAX_TEXT:
        raise ValueError('Extracted text exceeds the safe reading limit.')
    return segments, warnings


def import_source(source, project, kind='screenplay'):
    if kind not in ('screenplay', 'adaptation'):
        raise ValueError('Choose screenplay or adaptation as the source purpose.')
    path = Path(source).expanduser().resolve()
    if not path.is_file(): raise ValueError('Choose an existing source file.')
    fmt = FORMATS.get(path.suffix.lower())
    if not fmt: raise ValueError('Supported files: FDX, Fountain, TXT, MD, DOCX, and text-based PDF.')
    if path.stat().st_size > MAX_SOURCE: raise ValueError('Source exceeds the 50 MB import limit. Split it into labeled parts.')
    data = path.read_bytes()
    if len(data) > MAX_SOURCE: raise ValueError('Source exceeds the 50 MB import limit.')
    segments, warnings = extract(data, fmt, path)
    has_text = any(item['text'].strip() for item in segments)
    status = 'extracted_needs_review' if has_text else ('needs_ocr_or_text_copy' if fmt == 'pdf' else 'empty_source')
    if not has_text: warnings.append('No readable text was extracted. Do not diagnose or adapt the source until a readable copy is supplied.')
    root = Path(project).resolve()
    destination = root / 'sources' / 'private' / (datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ') + '-' + uuid.uuid4().hex[:12])
    # Private inputs must never be redirected into a tracked/shared directory.
    for ancestor in (root / 'sources', root / 'sources/private'):
        if ancestor.is_symlink(): raise ValueError('The source storage directory cannot be a symbolic link.')
    destination.mkdir(mode=0o700, parents=True, exist_ok=False)
    original = destination / ('original' + path.suffix.lower())
    original.write_bytes(data)
    original.chmod(0o600)
    payload = {'schema_version': 1, 'source_sha256': digest(data), 'segments': segments}
    (destination / 'segments.json').write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    reading = '\n\n'.join('[' + item['location'] + (': ' + item['type'] if 'type' in item else '') + ']\n' + item['text'] for item in segments)
    (destination / 'reading.txt').write_text(reading, encoding='utf-8')
    manifest = {'schema_version': 1, 'import_id': destination.name, 'purpose': kind, 'format': fmt, 'original_name': path.name, 'original_file': original.name, 'source_sha256': digest(data), 'source_bytes': len(data), 'reading_sha256': digest(reading.encode('utf-8')), 'segment_count': len(segments), 'status': status, 'reading_completeness': 'not yet checked against original', 'warnings': warnings, 'next_step': 'Read the source and check extraction completeness. Then use story-studio for a screenplay diagnosis.' if kind == 'screenplay' else 'Read and inventory the source before adaptation. Establish adaptation permission/status, fidelity, dramatic spine, omissions, inventions, and source-to-scene links. Importing is not permission to publish.'}
    (destination / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    for child in destination.iterdir(): child.chmod(0o600)
    destination.chmod(0o700)
    return destination, manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source')
    parser.add_argument('--project', default='.')
    parser.add_argument('--kind', choices=['screenplay', 'adaptation'], default='screenplay')
    args = parser.parse_args()
    try:
        folder, report = import_source(args.source, args.project, args.kind)
    except (ValueError, OSError) as exc:
        parser.exit(2, f'Import stopped: {exc}\n')
    print(json.dumps({'folder': str(folder), **report}, ensure_ascii=False, indent=2))
    return 0 if report['status'] == 'extracted_needs_review' else 2


if __name__ == '__main__':
    raise SystemExit(main())
