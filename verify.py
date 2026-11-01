"""Verify exact source-to-HTML text, order, artwork sequence, and local assets."""
from pathlib import Path
from html.parser import HTMLParser
import re
ROOT=Path(__file__).resolve().parent
class Reader(HTMLParser):
    def __init__(self):
        super().__init__();self.paras=[];self.current=None;self.refs=[];self.ids=[];self.stages=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'data-paragraph' in a:self.current=''
        if 'id' in a:self.ids.append(a['id'])
        if tag=='section':self.stages.append(a['id'])
        for k in ('src','href'):
            if k in a:self.refs.append(a[k])
    def handle_data(self,data):
        if self.current is not None:self.current+=data
    def handle_endtag(self,tag):
        if tag=='p' and self.current is not None:self.paras.append(self.current);self.current=None
r=Reader();r.feed((ROOT/'index.html').read_text())
source=(ROOT/'essay.md').read_text().strip().split('\n\n')
expected=[x.replace('**','').replace('*','') for x in source[2:]]
assert r.paras==expected,'Essay paragraph mismatch'
assert r.stages==['body','awareness','transition','continuity','galaxy']
for ref in r.refs:
    if ref.startswith('#'): assert ref[1:] in r.ids, ref
    elif not ref.startswith('https://'): assert (ROOT/ref).is_file(),ref
assert 'prefers-reduced-motion:reduce' in (ROOT/'styles.css').read_text()
assert r.paras[-1].endswith('once the organization that made us individuals has ended.')
print(f'PASS: {len(expected)} exact paragraphs in order; five ordered stages; all local paths and anchors; reduced-motion rule; exact ending.')
