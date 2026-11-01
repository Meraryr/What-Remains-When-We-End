"""Rebuild the page from the approved essay using Python 3 (no dependencies)."""
from pathlib import Path
import html, re, argparse
parser = argparse.ArgumentParser()
parser.add_argument("--base-url", default="https://meraryr.github.io/What-Remains-When-We-End/", help="Public project URL for canonical and social metadata")
args = parser.parse_args()
ROOT = Path(__file__).resolve().parent
blocks = (ROOT / 'essay.md').read_text().strip().split('\n\n')
def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    return re.sub(r'\*(.+?)\*', r'<em>\1</em>', s)
# Exact paragraph anchors: markers are navigation, never editorial headings.
anchors = ['What if death is not', 'Our bodies perform', 'And this brings us back', '**This leads to my central proposal', 'Suddenly, the question']
starts = [next(i for i,b in enumerate(blocks) if b.startswith(a)) for a in anchors]
labels = ['The Body','Awareness and Exchange','The Transition','The Continuity','What Remains']
ids = ['body','awareness','transition','continuity','galaxy']
alts = ['Solid human form from the original transformation artwork.', 'Changed human form from the original transformation artwork.', 'Skeletal human organization from the original transformation artwork.', 'Dispersing human traces and particles from the original transformation artwork.', 'Spiral galaxy from the original transformation artwork.']
nav=''.join(f'<a href="#{id}" aria-label="{i+1:02} — {label}" title="{label}"><span class="dot"></span><span class="nav-number">{i+1:02}</span><span class="nav-label">{label}</span></a>' for i,(id,label) in enumerate(zip(ids,labels)))
sections=[]
for i,(id,label) in enumerate(zip(ids,labels)):
    paras=[]
    for j in range(starts[i], starts[i+1] if i<4 else len(blocks)):
        cls='statement' if blocks[j].startswith('**') and blocks[j].endswith('**') else ''
        if j==2: cls+=' lead'
        if j==len(blocks)-1: cls+=' final-question'
        if j==84: paras.append('<img class="closing-art" src="assets/galaxy.webp" width="680" height="350" alt="Spiral galaxy from the original transformation artwork." loading="lazy">')
        paras.append(f'<p class="{cls.strip()}" data-paragraph="{j}">{inline(blocks[j])}</p>')
    sections.append(f'''<section class="movement movement-{i+1}" id="{id}" aria-label="{label}">
    <div class="movement-marker" aria-hidden="true"><span>{i+1:02} / 05</span><span>{label}</span></div>
    <figure class="art"><img src="assets/{id}.webp" width="690" height="{[170,280,280,549,350][i]}" alt="{alts[i]}" {'fetchpriority="high"' if i==0 else 'loading="lazy"'}><figcaption><span>{i+1:02}</span><span>{label}</span><span>↗</span></figcaption></figure>
    <div class="prose">{''.join(paras)}</div></section>''')
page=f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>What Remains When We End? — Merary Rodríguez</title>
<meta name="description" content="Consciousness, Bioelectricity, and the Architecture of Becoming. An essay by Merary Rodríguez, More Human Than Human Project.">
<meta name="author" content="Merary Rodríguez"><meta name="theme-color" content="#000000">
<meta property="og:type" content="article"><meta property="og:title" content="What Remains When We End?"><meta property="og:description" content="Consciousness, Bioelectricity, and the Architecture of Becoming — Merary Rodríguez"><meta property="og:image" content="assets/social-preview.jpg"><meta property="og:image:alt" content="What Remains When We End? Original human transformation artwork on black."><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="What Remains When We End?"><meta name="twitter:description" content="An essay by Merary Rodríguez — More Human Than Human Project"><meta name="twitter:image" content="assets/social-preview.jpg">
<link rel="icon" href="assets/icon.png"><link rel="apple-touch-icon" href="assets/icon.png"><link rel="stylesheet" href="styles.css"><script src="script.js" defer></script></head>
<body><a class="skip" href="#body">Skip to essay</a><div class="reading-progress" aria-hidden="true"></div>
<header class="masthead"><a href="#top">More Human Than Human <span>Project</span></a><span class="masthead-right">An essay by Merary Rodríguez</span></header>
<nav class="stage-nav" aria-label="Essay movements">{nav}</nav>
<main id="top"><div class="hero"><div class="eyebrow">Merary Rodríguez <span>Independent Researcher</span></div><h1 data-source="title">{inline(blocks[0][2:])}</h1><p class="subtitle" data-source="subtitle">{inline(blocks[1])}</p><div class="hero-bottom"><a href="#body">Read the essay <span>↓</span></a><span>01 — 05 / A continuous reading</span></div></div>
<article aria-label="What Remains When We End?">{''.join(sections)}</article></main></body></html>'''
if args.base_url:
    base = args.base_url.rstrip('/') + '/'
    if not base.startswith('https://'): raise ValueError('Public base URL must use HTTPS')
    page = page.replace('content="assets/social-preview.jpg"', 'content="'+html.escape(base, quote=True)+'assets/social-preview.jpg"')
    page = page.replace('</head>', '<link rel="canonical" href="'+html.escape(base, quote=True)+'"><meta property="og:url" content="'+html.escape(base, quote=True)+'"></head>')
(ROOT/'index.html').write_text(page)
print(f'Built {len(blocks)-2} original paragraphs in five continuous movements.')
