# What Remains When We End?

**Merary Rodríguez — Independent Researcher**  
**More Human Than Human Project**

A continuous, static reading experience for *Consciousness, Bioelectricity, and the Architecture of Becoming*.

## Preview and maintain

Run `python3 -m http.server 8765 --bind 127.0.0.1` from this directory and open `http://127.0.0.1:8765/`. The page also works directly from `index.html` without a server. No packages, backend, analytics, external fonts, APIs, or network assets are required.

`essay.md` is the source of truth. It is an unchanged copy of the approved essay. Do not edit generated essay paragraphs in `index.html`. After an author-approved source change, run:

```
python3 build.py
python3 verify.py
```

The builder preserves paragraph order, inline emphasis, title, and subtitle. Its five exact paragraph anchors position navigation markers without adding essay headings. If an approved revision changes an anchor, update the corresponding anchor in `build.py`.

## Artwork

`assets/original-transformation.jpg` preserves the supplied original unmodified. WebP crops reveal its sequence in reading order: solid body, changed body, skeleton, dissolving traces then dispersed particles, galaxy. Adjacent-form remnants are masked only in derivative crops. The original orientation of each figure is preserved. The layout reference guided composition; it is not served as a page background. Social artwork combines the supplied solid-body crop with the supplied title and attribution. The small navigation-style icon is a generated geometric UI asset.

Desktop illustrations remain beside their corresponding prose. Mobile artwork enters the document flow; the galaxy sits immediately before the final two paragraphs. All essay content is available without JavaScript. JavaScript only updates the progress bar and active navigation marker. Reduced-motion CSS disables smooth scrolling and transitions.

## Publishing and updates

Repository: https://github.com/Meraryr/What-Remains-When-We-End

Website: https://meraryr.github.io/What-Remains-When-We-End/

Publication was approved by the author. GitHub Pages serves the `main` branch from the repository root. `.nojekyll` enables direct static serving. Push approved updates to `main` to redeploy.

The builder defaults to the public project URL, preserving absolute social-preview URLs and canonical metadata on every rebuild. If the hosting address changes, use:

```
python3 build.py --base-url https://YOUR-NEW-PUBLIC-URL/
python3 verify.py
```

Only this standalone repository belongs to this website. Do not include credentials, unrelated research, or other repository content. No license is granted to the writing or artwork.

## Repository files

- `index.html` — generated full essay and metadata
- `styles.css` — responsive layout and reduced-motion support
- `script.js` — reading progress and active navigation
- `essay.md` — exact approved source
- `build.py` — dependency-free source-to-page builder
- `verify.py` — text, sequence, and local-link checks
- `README.md` — public maintenance and publishing instructions
- `.nojekyll` — GitHub Pages static serving
- `assets/original-transformation.jpg` — unchanged original
- `assets/body.webp`, `assets/awareness.webp`, `assets/transition.webp`, `assets/continuity.webp`, `assets/galaxy.webp` — artwork derivatives
- `assets/social-preview.jpg` — sharing image
- `assets/icon.png` — mobile/browser icon

No open-source license is granted by this package.
