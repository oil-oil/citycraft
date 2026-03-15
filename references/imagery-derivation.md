# Imagery Derivation Guide

When a user describes a vibe, scene, era, or material — rather than picking a city — use this guide to translate that description into a concrete design system.

The process: **extract sensory signals → map to design axes → pick exact values**.

---

## Step 1: Extract Sensory Signals

Read the description and note what it implies across five senses:

| Sense | What to listen for |
|-------|-------------------|
| **Light** | Harsh/soft, warm/cool, artificial/natural, dim/bright |
| **Texture** | Rough/smooth, aged/pristine, matte/glossy, organic/industrial |
| **Sound** | Silence, hum, crackling, bass, echo (maps to pace + density) |
| **Time** | Era, season, time of day, historical period |
| **Emotion** | Tension, nostalgia, wonder, intimacy, awe, danger |

---

## Step 2: Map to Design Axes

### Color Temperature & Value

| Signal | Background direction | Accent direction |
|--------|---------------------|------------------|
| Warm light (candle, sunset, tungsten) | `#1c100a` → `#f5e8d0` range | Amber `#c9883a`, terracotta `#c05738` |
| Cool light (neon, moonlight, fluorescent) | `#060b14` → `#e8f0f5` range | Electric cyan `#00d4ff`, icy violet `#a78bfa` |
| Natural light (forest, overcast) | `#0d1a0d` → `#edf5ec` range | Moss `#6db86b`, sage `#8fad8f` |
| No light / night | `#050507` range | Any vivid accent for contrast |
| Aged / faded | Desaturate everything ±30% | Sepia `#c9a882`, rust `#b56c3a` |

### Typography

| Era / Feeling | Display font | Body font | Style notes |
|---------------|-------------|-----------|-------------|
| Pre-1960 / classical | Cormorant Garamond, Playfair Display | Georgia | Italic headlines, generous leading |
| 1960s–70s / retro | Anton, Impact | Helvetica Neue | Compressed, all-caps headlines |
| 1980s / sci-fi magazine | Space Grotesk, Bebas Neue | IBM Plex Mono | Uppercase, tight tracking |
| 1990s / grunge/indie | A mix of serif + slab | System UI | Irregular sizing, rotated elements |
| 2000s / early digital | VT323, IBM Plex Mono | sans-serif | Pixelated, monospaced |
| Contemporary clean | Plus Jakarta Sans, Inter | Same family lighter | Large scale, ultra-tight tracking |
| Handmade / artisan | Playfair Display italic | DM Serif Display | Mixed weights, no tracking |
| East Asian influenced | Noto Serif SC (CJK) | System UI | Vertical rhythm, more line-height |

### Background Texture

| Signal | CSS approach |
|--------|-------------|
| Paper / aged / analog | SVG `feTurbulence` noise + subtle sepia gradient |
| Industrial / concrete | Repeating diagonal or crosshatch lines, desaturated |
| Digital / grid | CSS `linear-gradient` grid lines, very low opacity |
| Natural / organic | Radial gradients of 2–3 muted tones, no hard edges |
| Glossy / luxury | Very subtle `radial-gradient` from center, near-black to `#1a1a1a` |
| Scanlines / CRT | Repeating 2px stripes, 3% opacity |
| Linen / textile | SVG diagonal weave, warm base |

### Motion Character

| Feeling | GSAP approach |
|---------|--------------|
| Weightless / dreamy | Long durations (1.2–1.8s), `ease: "power1.out"`, opacity-only |
| Mechanical / precise | Short snappy (0.3s), `ease: "back.out(1.4)"`, x/y translations |
| Dramatic / cinematic | Scale from 1.05→1, blur entrance, `ease: "expo.out"` |
| Natural / organic | Stagger with slight rotation (±3°), `ease: "sine.inOut"` |
| Electric / fast | 0.15–0.25s, `ease: "power4.out"`, clip-path wipes |
| Nostalgic / slow | 1.5s+ fade, subtle y drift, no bounce |

---

## Step 3: Worked Examples

### "1970年代科幻杂志封面"
- **Light**: Harsh, artificial, chromatic
- **Texture**: Offset print, slightly misregistered, halftone
- **Era**: 1970s
- **Emotion**: Wonder, retro-future

Derived design system:
```css
--bg-base: #0d0a1a;           /* deep inky purple-black */
--bg-surface: #1a1530;
--color-primary: #ff6b35;     /* orange-red — classic pulp accent */
--color-secondary: #00d4ff;   /* electric cyan */
--font-display: 'Anton', 'Impact', sans-serif;  /* compressed, strong */
--font-body: 'IBM Plex Mono', monospace;        /* typewriter feel */
```
Texture: halftone dots via `radial-gradient(circle, rgba(255,107,53,0.15) 1px, transparent 1px)` at `background-size: 6px 6px`
Motion: Snappy clip-path reveals, stagger 0.08s, `ease: "power4.out"`

---

### "深夜的二手书店"
- **Light**: Warm amber pools, dark corners
- **Texture**: Worn paper, wood grain, dust
- **Era**: Timeless, analog
- **Emotion**: Intimacy, nostalgia, quiet

Derived design system:
```css
--bg-base: #0d0904;
--bg-surface: #1c140c;
--color-primary: #c9883a;     /* warm gold */
--color-secondary: #8fad8f;   /* muted sage — faded book spines */
--font-display: 'Cormorant Garamond', Georgia, serif;
--font-body: 'Plus Jakarta Sans', sans-serif;
```
Texture: SVG `feTurbulence` noise at 4% opacity over warm base
Motion: Slow dissolves (1.4s), `ease: "power1.inOut"`, y drift -20px

---

### "热带雨林 + 极简主义"
- **Light**: Dappled green, diffuse
- **Texture**: Living, breathing, but never cluttered
- **Emotion**: Calm vitality, presence

Derived design system:
```css
--bg-base: #f5f7f2;           /* near-white with green cast */
--bg-surface: #edf2e8;
--color-primary: #1a5c3a;     /* deep forest green */
--color-secondary: #8fad8f;
--font-display: 'Playfair Display', serif;
--font-body: 'Plus Jakarta Sans', sans-serif;
```
Texture: Radial gradient of two muted greens, `background-size: 100% 100%`
Motion: Organic stagger (0.12s), slight rotation (2°), `ease: "sine.out"`

---

### "上海1930年代的霓虹"
- **Light**: Neon signs, wet pavement reflections
- **Texture**: Art Deco geometry, lacquer, chrome
- **Era**: 1930s, Shanghai
- **Emotion**: Glamour, tension, modernity

Derived design system:
```css
--bg-base: #08060c;
--bg-surface: #110e18;
--color-primary: #e8c84a;     /* gold neon */
--color-secondary: #c0392b;   /* red lantern */
--font-display: 'Playfair Display', Georgia, serif;
--font-body: 'Cormorant Garamond', serif;
```
Texture: Very subtle grid lines (Art Deco) + warm radial glow at top
Motion: Dramatic scale reveals (1.04→1), `ease: "expo.out"`, long stagger 0.18s

---

### "斯堪的纳维亚冬日"
- **Light**: Flat, grey-white, diffuse
- **Texture**: Raw concrete, birch wood, linen
- **Emotion**: Austere warmth, functional beauty

Derived design system:
```css
--bg-base: #f0ede8;
--bg-surface: #faf8f5;
--color-primary: #2c2c2c;
--color-secondary: #c05738;   /* stove-red — single warm accent */
--font-display: 'Plus Jakarta Sans', sans-serif;
--font-body: Same, lighter weight;
```
Texture: Very fine linen repeating diagonal, 2% opacity
Motion: Restrained, no bounce, `ease: "power2.inOut"`, y drift only

---

## Step 4: Blending Multiple Descriptions

When users combine two vibes (e.g. "京都的质感 + 首尔的配色"):
- Take **texture** and **typography** from the dominant aesthetic (listed first)
- Take **color palette** and **accent** from the modifier aesthetic (listed second)
- Take **motion** from whichever feels more "alive" in the context

When signals conflict (e.g. "luxury + brutalist"):
- Use the tension as the design concept: dark industrial base + single gold accent
- Let the contrast be intentional, not compromised

---

## Quick Reference: Signal → Token

| User says | Background | Primary font | Accent |
|-----------|-----------|-------------|--------|
| 科幻 / 宇宙 | `#060b14` | Space Grotesk | `#00e5ff` |
| 复古 / 年代 | `#1c100a` | Cormorant Garamond | `#c9883a` |
| 奢华 / 黄金 | `#080806` | Playfair Display | `#c9a54a` |
| 工业 / 混凝土 | `#141414` | Anton | `#ff5533` |
| 自然 / 森林 | `#0d1a0d` | Plus Jakarta Sans | `#6db86b` |
| 极简 / 留白 | `#f5f5f3` | Plus Jakarta Sans | `#1a1a1a` |
| 梦幻 / 柔和 | `#fdf0f5` | Cormorant Garamond italic | `#e8829a` |
| 东方 / 国风 | `#120a06` | Noto Serif SC | `#c0392b` |
| 地中海 / 夏天 | `#f0f8ff` | Plus Jakarta Sans | `#1a6fa8` |
| 霓虹 / 上海 | `#08060c` | Playfair Display | `#e8c84a` |
| 二手书店 | `#0d0904` | Cormorant Garamond | `#c9883a` |
| 斯堪的纳维亚 | `#f0ede8` | Plus Jakarta Sans | `#c05738` |
| 赛博朋克 | `#050812` | IBM Plex Mono | `#ff2d78` |
| 1970s sci-fi | `#0d0a1a` | Anton | `#ff6b35` |
