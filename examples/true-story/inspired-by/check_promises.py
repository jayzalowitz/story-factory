#!/usr/bin/env python3
"""Check actual current receipts and rejection of an editorially rejected label."""
import json
from pathlib import Path
import shutil
import sys
import tempfile
sys.path.insert(0,str(Path(__file__).resolve().parents[3]))
from story_factory.story_check import quality_problems,truth_problems
root=Path(__file__).resolve().parent
errors=truth_problems(root,True)+quality_problems(root)
if errors:raise SystemExit('\n'.join(errors))
with tempfile.TemporaryDirectory() as location:
    trial=Path(location)/'rejected'
    shutil.copytree(root,trial)
    mode=json.loads((trial/'research/source_mode.json').read_text())
    mode['mode']='based-on';mode['audience_wording']="Based on the true story of Jo and Inez's final pool recording."
    (trial/'research/source_mode.json').write_text(json.dumps(mode))
    shutil.copyfile(trial/'research/rejected_based_on_review.json',trial/'research/truth.json')
    rejected=truth_problems(trial,True)
    if 'Truth review requires revision' not in rejected:raise SystemExit('Rejected editorial verdict was not blocked')
print('Current inspired-by truth and craft receipts pass. The recorded false based-on promise is blocked as REVISE. This gate does not independently judge historical or artistic truth.')
