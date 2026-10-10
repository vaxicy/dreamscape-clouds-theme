<p align="center">
  <img src="https://raw.githubusercontent.com/vaxicy/dreamscape-clouds-theme/main/logo/logo128.png" width="128" alt="Dreamscape Clouds Theme icon">
</p>

<h1 align="center">Dreamscape Clouds Theme</h1>

<p align="center">A dreamy pastel Chrome theme blending soft lilac, airy blue and icy aqua.</p>

<p align="center">
  <img src="https://img.shields.io/badge/Chrome%20Web%20Store-theme-blue?logo=googlechrome" alt="Chrome Web Store">
  <img src="https://img.shields.io/badge/version-1.0.0-blue" alt="version">
  <img src="https://img.shields.io/badge/license-Non--Commercial-lightgrey" alt="license">
</p>

## About

Dreamscape Clouds Theme brings a quiet sky to Chrome. A soft pastel lilac frame wraps the top of the window, the toolbar and active tab cool into icy aqua, and the new tab page opens on pale blue so the page you are reading stays the brightest thing on screen. Deep blue-violet text keeps tab titles, bookmark labels, toolbar icons and the address bar sharp on the light surfaces, and deep lilac marks the new tab header and every link. Active and inactive windows share one frame colour, so nothing shifts when the window loses focus. The design is flat colour throughout — no wallpaper, no textures, no gradients — and the transparent icon distils it into a tall lilac crescent above a low blue cloud, with a star and two drifting mist lines.

## Color Palette

| Color | Hex | Usage |
|-------|-----|-------|
| Pastel Lilac | `#CDC6ED` | Window frame (active and inactive) and window button background |
| Icy Aqua | `#E5F3F4` | Toolbar, active tab, bookmarks bar |
| Cool White | `#F7FBFC` | Omnibox (address bar) field |
| Pale Sky | `#F0F5FC` | New tab page background |
| Blue Violet Ink | `#39354F` | Tab, bookmark, toolbar and new-tab text, toolbar icons |
| Deep Lilac | `#70559A` | New tab page header and links |
| Orchid Lilac | `#DAB1F0` | Small star dot in the logo |
| Pale Lilac | `#E2CFF4` | Lower mist line in the logo |
| Cloud Blue | `#C5DAF6` | Cloud fill and upper mist line in the logo |
| Soft Blue | `#B6C7EF` | Star in the logo |

The first six rows are the browser surfaces set in `manifest.json`. The last four are artwork tones: they live in the icon and in the store previews, and are deliberately kept out of the browser chrome where a paler tint would drop below readable contrast.

## Chrome UI notes

Not every pixel in the window comes from the manifest — Chrome and the operating system paint some of them — so the store previews follow what a real install renders:

- **Google wordmark on the new tab page:** drawn by Chrome as a single flat tint computed from the new tab background, so it appears soft blue here rather than as the four-colour brand mark.
- **Shortcut tiles:** Chrome tints the round shortcut buttons the same way, so they pick up the same pale blue tone instead of a fixed brand colour.
- **Window buttons, hover fills and separators:** painted by Chrome and Windows, and left in their own neutral tones on the lilac frame.
- **Address bar:** a white field with Chrome's own focus outline, which stays legible against the icy aqua toolbar.
- **AI cards and the *Customize Chrome* button:** Chrome's own dark surfaces, untouched by the theme.

## Features

- Soft pastel lilac frame with an icy aqua toolbar and active tab for calm, readable browser chrome.
- Flat, solid colour design with no wallpaper, textures or gradients.
- Pale sky new tab page with deep blue-violet text and deep lilac header and links.
- One continuous frame colour whether the window is focused or not.
- Single-tone Google wordmark drawn by Chrome itself through `ntp_logo_alternate`.
- Pure theme: no scripts, no permissions, nothing collected.

## Install

### From source (unpacked)

1. Download or clone this repository.
2. Open Chrome and navigate to `chrome://extensions`.
3. Enable **Developer mode** in the top-right corner.
4. Click **Load unpacked** and select this folder.
5. The theme applies immediately; reset it any time under Settings, then Appearance, then Themes.

### From the Chrome Web Store

The store listing is in preparation. Until it is live, load the unpacked copy with the steps above.

## Preview

### Store screenshots · 1280×800

**Browser interface** — the themed window with a bookmarks bar and the new tab page.

![Dreamscape Clouds Theme browser preview](https://raw.githubusercontent.com/vaxicy/dreamscape-clouds-theme/main/store-assets/screenshots/en/screenshot-1-browser.png)

**Palette & highlights** — the tones the theme is built from and what each one controls.

![Dreamscape Clouds Theme palette](https://raw.githubusercontent.com/vaxicy/dreamscape-clouds-theme/main/store-assets/screenshots/en/screenshot-2-introduction.png)

### Store promo tiles

**Marquee tile · 1400×560** — “Soft lilac. Airy blue. A little calm above the clouds.”

![Dreamscape Clouds Theme marquee](https://raw.githubusercontent.com/vaxicy/dreamscape-clouds-theme/main/store-assets/promo/1400x560.png)

**Small tile · 440×280** — “A quiet sky for your everyday browsing.”

<p align="center">
  <img src="https://raw.githubusercontent.com/vaxicy/dreamscape-clouds-theme/main/store-assets/promo/440x280.png" width="440" alt="Dreamscape Clouds Theme promo tile">
</p>

These are illustrative English HTML/CSS layouts rendered by headless Chromium and calibrated against a real installed Chrome session. Browser surfaces take their colours from `manifest.json`; the Chrome-painted details — the blue Google wordmark and shortcut circles, the white search field, the dark AI cards and the dark *Customize Chrome* button — follow the reference browser, and the sampled tones are listed in [`store-assets/ASSET-NOTES.md`](store-assets/ASSET-NOTES.md). Tabs and bookmarks use generic English labels. These are not native captures, so controls and new tab content can vary by browser version and operating system.

## Files

| File | Description |
|------|-------------|
| `manifest.json` | Chrome theme manifest (MV3) with an inline `theme` block — single source of truth for every colour |
| `logo/logo128.png` | Theme and store icon, 128x128, the only size the manifest references |
| `store-assets/screenshots/en/` | Store listing screenshots (1280x800) |
| `store-assets/promo/` | Promo tiles (440x280 and 1400x560) |
| `store-assets/references/` | The browser, introduction and promo mock-up HTML plus their PNG renders |
| `store-assets/ASSET-NOTES.md` | Calibration notes: which tones are manifest colours and which are sampled from Chrome |
| `store-assets/store-description.txt` | Store listing copy (English) |
| `scripts/generate-logo.py` | Draws the transparent 128x128 icon with Pillow |
| `scripts/generate-store-assets.py` | Renders both screenshots and both promo tiles from `manifest.json` colours |
| `scripts/requirements.txt` | Python dependencies for the asset generators |
| `scripts/package.ps1` | Builds the release ZIPs |
| `LICENSE` | Non-Commercial License (bilingual) |

## Regenerating the assets

```
pip install -r scripts/requirements.txt
playwright install chromium

python scripts/generate-logo.py
python scripts/generate-store-assets.py
```

The logo script exports only `logo/logo128.png` with a transparent background and antialiased edges. The store generator renders all four assets in one pass — both screenshots and both promo tiles — and keeps the HTML sources in `store-assets/references/`, so a style change is made in the script and re-rendered, never patched onto a PNG. The approved logo is read from disk and is not redrawn by the store generator.

## Packaging

```
powershell -ExecutionPolicy Bypass -File scripts/package.ps1 -Force
```

Writes one ZIP to the default folder `D:\迅雷下载\vibe coding`: `dreamscape-clouds-theme-1.0.0.zip`, holding the complete project with `manifest.json` at the archive root, so the same archive is what the Chrome Web Store upload form takes. `-Force` overwrites an existing archive.

The script checks the manifest inside the ZIP against this project, confirms that every file the manifest references is present, and rejects repository metadata, local caches and nested archives. The screenshots and promo tiles travel inside the ZIP, but the store form still needs them uploaded one by one: `store-assets/screenshots/en/` fills the two screenshot slots, `store-assets/promo/1400x560.png` is the marquee tile and `store-assets/promo/440x280.png` is the small tile.

## License

Non-Commercial License — personal use permitted, commercial use requires permission. See [LICENSE](LICENSE).
