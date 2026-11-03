from pathlib import Path
from html.parser import HTMLParser
from collections import Counter
import json,re
ROOT=Path(__file__).parent;D=ROOT/'dist'
c=json.loads((D/'catalog.json').read_text());tasks=c['tasks'];assert len(tasks)==40 and len({t['id'] for t in tasks})==40
assert Counter(t['arm'] for t in tasks)=={'single':20,'dual':20}
assert Counter(t['category'] for t in tasks)=={k['id']:8 for k in c['categories']}
assert sum(t['episodes'] for t in tasks if t['arm']=='single')==1000
assert sum(t['publishedEpisodes'] for t in tasks)==416
assert sum(bool(t['drive']) for t in tasks)==37
assert sum(bool(t['video']) for t in tasks)==20
for t in tasks:
 assert t['instruction'] and t['name'] and t['fps']>0
 for key in ['image','video']:
  if t.get(key): assert (D/t[key]).is_file() and (D/t[key]).stat().st_size>0,(t['id'],key)
 for key in ['drive','github']:
  if t.get(key):assert t[key].startswith('https://')
 if t['arm']=='dual':
  assert t['sourceEpisodes']==t['driveRecordEpisodes']==50
  assert t['publishedEpisodes']==(50 if t['category']=='01_conditional' else 1)
  assert len(t['driveReviewVideos'])==5 and t['driveFullTrainingStreamsIncluded'] is False
js=(D/'catalog.js').read_text();assert json.loads(js.removeprefix('window.BENCHMARK = ').strip().removesuffix(';'))==c
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.links=[];self.assets=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id'in a:self.ids.append(a['id'])
  if tag=='a' and 'href'in a:self.links.append(a['href'])
  if 'src'in a:self.assets.append(a['src'])
  if tag=='link' and 'href'in a:self.assets.append(a['href'])
p=Parser();p.feed((D/'index.html').read_text());assert len(p.ids)==len(set(p.ids))
for link in p.links:
 if link.startswith('#') and len(link)>1:assert link[1:] in p.ids,link
for asset in p.assets:
 if not asset.startswith(('https:','data:')):assert (D/asset).exists(),asset
for f in D.glob('*'):
 if f.suffix in ['.html','.css','.js','.json']:
  text=f.read_text();assert not re.search(r'/(?:home|Users)/[^/]+/',text),str(f)
assert not any(f.is_symlink() for f in D.rglob('*'))
report={'passed':True,'tasks':40,'categories':5,'single_arm_tasks':20,'dual_arm_tasks':20,'canonical_single_arm_episodes':1000,'published_episodes':416,'dual_arm_drive_review_links':100,'verified_task_drive_links':37,'preview_videos':20,'static_assets_and_anchors_passed':True,'portable_relative_paths_passed':True,'total_static_bytes':sum(f.stat().st_size for f in D.rglob('*') if f.is_file())}
print(json.dumps(report,indent=2))
