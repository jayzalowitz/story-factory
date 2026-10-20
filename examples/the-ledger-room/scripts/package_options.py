#!/usr/bin/env python3
"""Choose the documents this project should deliver. Unselected templates may stay blank."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SECTIONS = ['logline_synopsis','treatment','character_breakdowns','tone_visual_world','comps_and_positioning','casting_notes','director_targets','producer_targets','awards_strategy','festival_strategy','budget_and_scope','scene_showcase','marketing_blurb','poster_taglines','appendix']
PITCHES = ['one_pager','actor_pitch','director_pitch','financier_pitch','producer_pitch','distributor_pitch','streamer_pitch','festival_pitch','awards_pitch','coproduction_pitch','public_funder_pitch','talent_rep_pitch','exhibitor_pitch','cultural_partnership_pitch','press_pitch','craft_pitch']


def defaults():
    return {'screenplay': True, 'sections': list(SECTIONS), 'pitches': list(PITCHES)}


def validate(data):
    if not isinstance(data, dict) or set(data) != {'screenplay','sections','pitches'}:
        raise ValueError('Package options need exactly screenplay, sections, and pitches')
    if type(data['screenplay']) is not bool:
        raise ValueError('screenplay must be true or false')
    for key, known in [('sections',SECTIONS),('pitches',PITCHES)]:
        values=data[key]
        if not isinstance(values,list) or any(not isinstance(v,str) or v not in known for v in values):
            raise ValueError(f'Unknown {key}; use package_options.py list for available names')
        if len(set(values)) != len(values):raise ValueError(f'Duplicate {key}')
    if not data['screenplay'] and not data['sections'] and not data['pitches']:
        raise ValueError('Select at least one document')
    return data


def load(root):
    path=root/'development/package_options.json'
    return validate(json.loads(path.read_text())) if path.exists() else defaults()


def output_names(options):
    return (['screenplay'] if options['screenplay'] else []) + (['studio-package'] if options['sections'] else []) + [name.replace('_','-') for name in options['pitches']]


def package_entry(root, options, write=False):
    if not options['sections']:return None
    if options['sections']==SECTIONS:return root/'package/studio_package.tex'
    original=root/'package/studio_package.tex'
    text=original.read_text()
    if '% Package sections' not in text:
        raise ValueError('Studio wrapper needs its % Package sections marker for selected assembly')
    text=text.split('% Package sections',1)[0]+'% Package sections (selected)\n'
    text+='\n\\newpage\n'.join('\\input{'+name+'}\n' for name in options['sections'])+'\n\\end{document}\n'
    path=root/'package/selected_studio_package.tex'
    if write and (not path.exists() or path.read_text()!=text):path.write_text(text)
    return path


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command',choices=['list','show','configure'])
    parser.add_argument('--project',type=Path,default=ROOT)
    parser.add_argument('--section',action='append',choices=SECTIONS)
    parser.add_argument('--pitch',action='append',choices=PITCHES)
    parser.add_argument('--no-sections',action='store_true')
    parser.add_argument('--no-pitches',action='store_true')
    group=parser.add_mutually_exclusive_group()
    group.add_argument('--without-screenplay',action='store_true')
    group.add_argument('--with-screenplay',action='store_true')
    args=parser.parse_args()
    try:
        if args.command=='list':print(json.dumps(defaults(),indent=2));return
        root=args.project.resolve();data=load(root)
        if args.command=='configure':
            if args.no_sections and args.section:raise ValueError('Choose --no-sections or --section, not both')
            if args.no_pitches and args.pitch:raise ValueError('Choose --no-pitches or --pitch, not both')
            if args.section is not None:data['sections']=args.section
            if args.pitch is not None:data['pitches']=args.pitch
            if args.no_sections:data['sections']=[]
            if args.no_pitches:data['pitches']=[]
            if args.without_screenplay:data['screenplay']=False
            if args.with_screenplay:data['screenplay']=True
            validate(data)
            path=root/'development/package_options.json';path.parent.mkdir(parents=True,exist_ok=True)
            path.write_text(json.dumps(data,indent=2)+'\n')
        print(json.dumps(data,indent=2))
    except (ValueError,OSError) as error:parser.exit(1,str(error)+'\n')


if __name__=='__main__':main()
