#!/usr/bin/env python3
"""Render the public deep guide and readable Markdown from one content source."""
import argparse
import html
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'docs/guide-content.json'


def inline(text):
    parts = re.split(r'(`[^`]+`|\*\*[^*]+\*\*)', text)
    return ''.join('<code>'+html.escape(p[1:-1])+'</code>' if p.startswith('`') and p.endswith('`') else
                   '<strong>'+html.escape(p[2:-2])+'</strong>' if p.startswith('**') and p.endswith('**') else
                   html.escape(p) for p in parts)


def markdown_link(url):
    if url.startswith('index.html'):
        return 'https://jayzalowitz.github.io/story-factory/' + url[len('index.html'):]
    if url.startswith('examples/'):
        return '../site/' + url
    return url


def blocks(items, mode):
    output = []
    for item in items:
        kind = item['type']
        if kind in ['p', 'note']:
            text = item['text']
            output.append(('<aside class="guide-note">' if kind == 'note' else '<p>')+inline(text)+('</aside>' if kind == 'note' else '</p>') if mode == 'html' else ('> ' if kind == 'note' else '')+text+'\n')
        elif kind == 'list':
            output.append('<ul>'+''.join('<li>'+inline(t)+'</li>' for t in item['items'])+'</ul>' if mode == 'html' else '\n'.join('- '+t for t in item['items'])+'\n')
        elif kind == 'links':
            output.append('<p class="guide-links">'+ ' · '.join('<a href="'+html.escape(x['href'], quote=True)+'">'+html.escape(x['label'])+'</a>' for x in item['items'])+'</p>' if mode == 'html' else ' · '.join('['+x['label']+']('+markdown_link(x['href'])+')' for x in item['items'])+'\n')
        elif kind == 'command':
            for prefix, host in [('/', 'Claude Code'), ('$', 'Codex')]:
                command = prefix+item['command']+' '+item['request']
                output.append('<div class="guide-command"><p class="gate-label">'+host+'</p><pre><code>'+html.escape(command)+'</code></pre></div>' if mode == 'html' else host+'\n\n```text\n'+command+'\n```\n')
        elif kind == 'table':
            headers, rows = item['headers'], item['rows']
            if mode == 'html':
                output.append('<div class="guide-table-wrap"><table><thead><tr>'+''.join('<th scope="col">'+inline(h)+'</th>' for h in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td data-label="'+html.escape(headers[i], quote=True)+'">'+inline(value)+'</td>' for i,value in enumerate(row))+'</tr>' for row in rows)+'</tbody></table></div>')
            else:
                clean=lambda t:t.replace('|', '\\|').replace('\n',' ')
                output.append('| '+' | '.join(map(clean,headers))+' |\n| '+' | '.join('---' for _ in headers)+' |\n'+'\n'.join('| '+' | '.join(map(clean,row))+' |' for row in rows)+'\n')
        elif kind == 'steps':
            if mode == 'html':
                output.append('<ol class="guide-stages">'+''.join('<li><h3>'+inline(row['title'])+'</h3>'+''.join('<p><strong>'+key.title()+':</strong> '+inline(row[key])+'</p>' for key in ['purpose','decision','record','check'])+'</li>' for row in item['items'])+'</ol>')
            else:
                output.append('\n'.join('### '+row['title']+'\n\n'+'\n\n'.join('**'+key.title()+':** '+row[key] for key in ['purpose','decision','record','check'])+'\n' for row in item['items']))
        elif kind == 'example':
            if mode == 'html':
                output.append('<div class="guide-example"><p class="gate-label">'+html.escape(item.get('label','ILLUSTRATIVE EXAMPLE'))+'</p><h3>'+inline(item['title'])+'</h3>'+''.join('<p><strong>'+label+':</strong> '+inline(item[key])+'</p>' for key,label in [('before','Before'),('after','Intervention'),('why','Why this changes the story')])+'</div>')
            else:
                output.append('### '+item['title']+'\n\n*'+item.get('label','Illustrative example')+'*\n\n'+'\n\n'.join('**'+label+':** '+item[key] for key,label in [('before','Before'),('after','Intervention'),('why','Why this changes the story')])+'\n')
        elif kind == 'details':
            output.append('<details class="guide-detail"><summary>'+inline(item['title'])+'</summary><div>'+blocks(item['blocks'],mode)+'</div></details>' if mode == 'html' else '<details>\n<summary>'+item['title']+'</summary>\n\n'+blocks(item['blocks'],mode)+'\n</details>\n')
        else:
            raise ValueError('Unknown guide block: '+kind)
    return '\n'.join(output)


def render():
    data=json.loads(SOURCE.read_text())
    sections=data['sections'];ids=[s['id'] for s in sections]
    if len(ids)!=len(set(ids)) or any(not re.fullmatch('[a-z][a-z0-9-]*',x) for x in ids):
        raise ValueError('Guide section IDs must be unique stable URL fragments')
    version=(ROOT/'VERSION').read_text().strip()
    download=f'https://github.com/jayzalowitz/story-factory/releases/download/v{version}/story-factory-{version}.zip'
    toc=''.join('<li><a href="#'+s['id']+'"><span>'+str(i+1).zfill(2)+'</span> '+html.escape(s['title'])+'</a></li>' for i,s in enumerate(sections))
    body=''.join('<section class="guide-section" id="'+s['id']+'" aria-labelledby="title-'+s['id']+'"><p class="eyebrow">'+str(i+1).zfill(2)+' / THE COMPLETE GUIDE</p><h2 id="title-'+s['id']+'">'+html.escape(s['title'])+'</h2><p class="guide-dek">'+inline(s['dek'])+'</p>'+blocks(s['blocks'],'html')+'<a class="guide-top" href="#contents">Back to contents ↑</a></section>' for i,s in enumerate(sections))
    page='''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="A practical guide to developing, revising, researching and packaging a screenplay with Story Factory."><meta name="referrer" content="no-referrer"><meta http-equiv="Content-Security-Policy" content="default-src 'self'; style-src 'self'; font-src 'self'; img-src 'self' data:; script-src 'none'; connect-src 'none'; object-src 'none'; base-uri 'self'; form-action 'none'"><title>Story Factory — The complete writing-room guide</title><link rel="icon" href="assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="style.css"></head>
<body class="guide-page"><a class="skip" href="#guide-main">Skip to the guide</a><div class="site-shell"><header class="masthead"><a class="brand" href="index.html#welcome"><span class="brand-mark" aria-hidden="true">sf.</span><span>Story Factory<span class="brand-note">The complete writing-room guide.</span></span></a><div class="header-actions"><a href="index.html#get-started">Get set up</a><a class="github-link" href="https://github.com/jayzalowitz/story-factory">GitHub ↗</a></div></header>
<main id="guide-main"><div class="guide-hero"><p class="eyebrow">FOR THE FIRST IDEA. AND THE FIFTH REWRITE.</p><h1>Go further<br><em>with the story.</em></h1><p class="guide-lead">'''+inline(data['intro'])+'''</p><p>Keep the one-command path when you want guidance. Come here when you want to understand a decision, challenge a draft, choose the right materials, or take more control.</p><div class="cover-actions"><a class="button" href="index.html#get-started">Start a project ↗</a><a class="text-link" href="'''+download+'''">Download the toolkit ↗</a></div></div>
<div class="guide-layout"><nav class="guide-contents" id="contents" aria-label="Guide contents"><h2>Find your next question</h2><ol>'''+toc+'''</ol><p>Read in order or jump to a topic. Every section has its own link. The practical examples are labeled as illustrative or drawn from an actual demonstration.</p></nav><div class="guide-reading">'''+body+'''</div></div></main><footer class="site-footer"><p>Story Factory · Your story, your decisions.</p><p><a href="index.html#welcome">Return to the introduction</a> · <a href="https://github.com/jayzalowitz/story-factory">GitHub</a> · <a href="'''+download+'''">Download</a></p></footer></div></body></html>\n'''
    md='# The complete Story Factory guide\n\n'+data['intro']+'\n\n[Read the designed website guide](https://jayzalowitz.github.io/story-factory/guide.html) · [Beginner setup](START_HERE.md) · [Commands](COMMANDS.md)\n\n'+ '\n'.join(str(i+1)+'. ['+s['title']+'](#'+s['id']+')' for i,s in enumerate(sections))+'\n\n'
    for s in sections:
        md+='\n<a id="'+s['id']+'"></a>\n\n## '+s['title']+'\n\n'+s['dek']+'\n\n'+blocks(s['blocks'],'md')+'\n'
    return {ROOT/'site/guide.html':page,ROOT/'docs/DEEP_DIVE.md':md.rstrip()+'\n'}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true');args=parser.parse_args()
    outputs=render()
    if args.check:
        stale=[str(p.relative_to(ROOT)) for p,text in outputs.items() if not p.exists() or p.read_text()!=text]
        if stale:parser.exit(1,'Guide outputs need rebuilding: '+', '.join(stale)+'\n')
        print('Guide HTML and Markdown match their shared source.')
    else:
        for path,text in outputs.items():path.write_text(text)
        print('Rendered the complete guide as HTML and Markdown.')

if __name__=='__main__':main()
