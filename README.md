# Placement Prep Vault (read-only Obsidian-style site)

A single-file website (`index.html`, no dependencies, no network calls) that presents the 246 markdown notes
of the vault (227 topic notes: 110 core plus 117 expansion notes, see `notes/Expansion Log.md`) the way Obsidian does, read-only.

**Features:** folder tree · `[[wikilinks]]` with hover previews · backlinks and outgoing links · tags ·
callouts, tables, task lists · code highlighting with copy buttons · LaTeX-style formulas · global and local
force-directed **graph view** (coloured by area, click to open, filter, zoom/pan/drag) · full-text search
(`Ctrl/⌘ K`, `tag:tier1`) · outline with scroll-spy · reading progress bar · "mark as studied" tracker with
per-area progress (saved in your browser) · previous/next · works on phones, tablets and desktops.

**Reading comfort:** open the **Aa** button for light / dark / auto theme, four text sizes, sans or serif body text and
three line widths (saved in your browser). Notes open with a reading-time estimate and a collapsible sub-topic list;
sub-topics are numbered, **Definition / Example / In the news / Interview angle** are colour-coded, and the news and
interview callouts are cards. On phones the sidebar and the outline/backlinks panel slide in as drawers, tables and
code scroll sideways inside their own box, the graph supports pinch-zoom, and a back-to-top button appears on long
notes. Printing a note from the browser gives a clean black-on-white page.

The graph view's spring and repulsion forces scale with the number of notes and links, and labels appear by link degree as you zoom, so the larger vault stays readable.

Shortcuts: `Ctrl/⌘ K` search, `G` graph, `Alt ←/→` previous/next note, `Esc` close previews.

## Layout

```
index.html          built site (this is what gets deployed)
src/template.html   site source: HTML + CSS + JS
notes/              the markdown vault (source of truth)
build.py            embeds notes/ into src/template.html -> index.html
vercel.json         static-site config
```

## Editing notes

Change or add `.md` files in `notes/` (keep note names unique), then run:

```bash
python3 build.py        # Python 3 only, no packages needed
```

and commit the regenerated `index.html`. Open `index.html` directly in a browser to preview.

## Put it on GitHub

1. Create an empty repository on github.com (e.g. `placement-prep-vault`), no README/licence.
2. In this folder:
   ```bash
   git init -b main
   git add .
   git commit -m "Placement prep vault site"
   git remote add origin https://github.com/<your-username>/placement-prep-vault.git
   git push -u origin main
   ```

## Deploy on Vercel

1. Go to https://vercel.com/new and import the GitHub repository.
2. Framework Preset: **Other**. Leave Build Command and Output Directory empty/default
   (the root `index.html` is served as-is). Root Directory: `./`.
3. Click **Deploy**. Every `git push` to `main` redeploys automatically.

(CLI alternative: `npm i -g vercel && vercel --prod` from this folder.)

Note: the studied tracker uses the browser's localStorage, so progress is per device/browser.
