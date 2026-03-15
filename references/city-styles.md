# City Style Reference

Each style is a complete design system — fonts, colors, textures, personality, and motion character.

---

## 1. 京都 (Kyoto)

**Emotional register**: Quiet precision. The beauty of things that age well. Restraint as richness.

### Fonts
- **Display**: `Noto Serif JP` or `Shippori Mincho` — for CJK headlines; `IM Fell English` — for Latin headlines
- **Body**: `Noto Sans JP` or `Inter` with letter-spacing: 0.02em

### Colors
```
--bg:           #f7f0e6    /* warm washi */
--bg-surface:   #ede4d6
--ink:          #2a1f14    /* sumi ink */
--ink-muted:    #7a6655
--accent:       #8b4513    /* persimmon */
--accent-soft:  #c9a882
--line:         rgba(42, 31, 20, 0.12)
```

### Texture
SVG noise with very low frequency, warm tint overlay. Crosshatch at ~2% opacity on surfaces. Paper-like.

```css
background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='200' height='200' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E");
```

### Layout character
- Generous whitespace. Sections breathe.
- Headlines at ~40% viewport width, left-aligned, with large leading
- Use vertical Japanese-style spacing rhythm
- Dividers: thin single lines (1px), not decorative shapes

### Motion character
- Slow, unhurried. `ease: "power2.inOut"`, durations 0.9–1.4s
- Elements fade in from a slight downward position, no blur
- No fast snaps or bounces

### Icons
- Thin stroke (1.5px), round linecap, inspired by Japanese mon (family crests)

---

## 2. 巴黎 (Paris)

**Emotional register**: Confidence without trying. The editorial eye. Pleasure in typography.

### Fonts
- **Display**: `Playfair Display` italic or `Cormorant Garamond` — large and proud
- **Body**: `Jost` or `DM Sans`
- **Accent text**: `Cormorant Garamond` italic for pull quotes

### Colors
```
--bg:           #f2ece0    /* crème */
--bg-surface:   #e8dfd0
--ink:          #1a1612    /* near-black with warmth */
--ink-muted:    #6b5f52
--accent:       #b5451b    /* vermillion */
--accent-soft:  #d4956a
--line:         rgba(26, 22, 18, 0.1)
```

### Texture
Very subtle halftone dot pattern at 1.5% opacity. Or a linen-weave CSS background pattern.

```css
background-image: repeating-linear-gradient(
  45deg,
  transparent,
  transparent 2px,
  rgba(26,22,18,0.015) 2px,
  rgba(26,22,18,0.015) 3px
);
```

### Layout character
- Editorial asymmetry: large pull quotes offset into the margin
- Oversized dropcaps or initial letters on section intros
- Mixed column widths — a wide text column next to a narrow annotation column
- Headlines can run up the left side vertically (rotated 90°)

### Motion character
- Elegant. `ease: "expo.out"`, durations 0.7–1.1s
- Text lines reveal upward from a clip mask (not fade — cut)
- Images scale from 95% → 100% on enter

### Icons
- Fine stroke (1px), slightly angular, editorial illustration style

---

## 3. 东京夜 (Tokyo Night)

**Emotional register**: Electric focus. The city that never sleeps. Precision under neon.

### Fonts
- **Display**: `Space Grotesk` bold or `Syne` — tight tracking, uppercase
- **Body**: `IBM Plex Mono` or `Geist Mono` for data-feel; or `Inter`
- **Accent**: Monospace for stats and numbers

### Colors
```
--bg:           #08060f    /* near-void */
--bg-surface:   #110d1e
--ink:          #f0ecff    /* cool white */
--ink-muted:    rgba(240,236,255,0.55)
--accent:       #7b5ef8    /* electric violet */
--accent-2:     #22d4a0    /* neon mint */
--accent-glow:  rgba(123, 94, 248, 0.25)
--line:         rgba(240,236,255,0.08)
```

### Texture
Radial gradient glows. Grid lines at ultra-low opacity. Scanline effect at 1%.

```css
background-image:
  linear-gradient(rgba(240,236,255,0.02) 1px, transparent 1px),
  linear-gradient(90deg, rgba(240,236,255,0.02) 1px, transparent 1px);
background-size: 48px 48px;
```

### Layout character
- Tight. Dense. Grid-locked.
- Numbers and stats as large typographic elements
- Sections separated by a single glowing horizontal line
- Accent elements have `box-shadow: 0 0 30px var(--accent-glow)`

### Motion character
- Fast and precise. `ease: "power3.out"`, durations 0.4–0.7s
- Elements snap into place from 20px below with no blur
- Stats count up with GSAP `textContent` tween
- Neon elements flicker in with a stagger

### Icons
- Thin stroke (1.5px), geometric, monospace-inspired. Some icons have a "glow" version (duplicate path at low opacity + blur filter).

---

## 4. 纽约 (New York)

**Emotional register**: No-nonsense authority. The city that doesn't explain itself.

### Fonts
- **Display**: `Anton` or `Bebas Neue` — ALL CAPS, compressed
- **Body**: `Haas Grotesk` or `Helvetica Neue` fallback stack: `"Helvetica Neue", Arial, sans-serif`
- Mix: display headlines in one weight, body text in a contrasting refined sans

### Colors
```
--bg:           #f0ede8    /* newsprint */
--bg-alt:       #1c1c1c    /* near-black */
--ink:          #111111
--ink-muted:    #555555
--accent:       #ff2d00    /* emergency red */
--accent-2:     #f5c518    /* taxi yellow */
--line:         #111111    /* full weight lines */
```

### Texture
Bold borders (2–3px solid black). No soft textures. Structure IS the decoration.

```css
/* Sections alternate between light and dark, divided by thick borders */
border-top: 3px solid var(--ink);
```

### Layout character
- Stark contrast between sections (light ↔ dark alternating)
- Oversized uppercase numerals as section markers (01, 02, 03)
- Text can run in multiple tight columns, newspaper-style
- Whitespace is deliberate and architectural, not generous

### Motion character
- Abrupt and confident. `ease: "power4.out"`, durations 0.3–0.5s
- No fades — elements cut in or wipe in
- Headings split into characters and stagger in fast

### Icons
- Bold stroke (2.5px), no rounded linecaps. Functional, industrial.

---

## 5. 首尔 (Seoul)

**Emotional register**: Warmly modern. Expressive restraint. Technology with soul.

### Fonts
- **Display**: `Pretendard` (Korean system) or `Plus Jakarta Sans` — medium-weight, not too heavy
- **Body**: `Pretendard` or `Outfit`
- Mix: Bold display, light body — contrast within the same family

### Colors
```
--bg:           #fafaf8    /* near-white with warmth */
--bg-surface:   #f2f0eb
--ink:          #191917
--ink-muted:    #6b6b63
--accent:       #3d5cff    /* cobalt */
--accent-2:     #ff6b35    /* tangerine */
--line:         rgba(25,25,23,0.1)
```

### Texture
Subtle gradient meshes. Soft shadow halos on cards. No harsh textures.

```css
background: radial-gradient(ellipse at 20% 50%, rgba(61,92,255,0.06) 0%, transparent 60%),
            radial-gradient(ellipse at 80% 20%, rgba(255,107,53,0.05) 0%, transparent 55%);
```

### Layout character
- Clean structure with one expressive breakout per section
- Color blocks used as compositional elements (a large solid-color square offset behind a photo)
- Rounded corners: `border-radius: 20px–32px` on cards and buttons

### Motion character
- Smooth and modern. `ease: "power2.out"`, durations 0.6–0.9s
- Cards scale up from 96% → 100% on enter
- Elements spring in with slight overshoot: `ease: "back.out(1.4)"`

### Icons
- Medium stroke (2px), rounded linecaps, friendly geometry. Some icons use a duotone fill.
---

## 6. 柏林 (Berlin)

**Emotional register**: Smelling damp concrete and cold night air while the muffled, rhythmic thump of a 4/4 bassline vibrates through a heavy steel door. It's unapologetically raw, stripping away the ornamental to reveal the brutal, highly functional, and intensely alive skeleton beneath.

### Fonts
- **Display**: `Druk Wide` — Aggressive, extended, and unyielding. It commands space with a stark, brutalist authority.
- **Body**: `Space Mono` — Adds a cold, technical, terminal-like precision that grounds the massive display type.
- *Accent note*: Use uppercase strictly for display headers, mimicking industrial stencil signage.

### Colors
```css
--line:         rgba(234, 234, 234, 0.12)
```

### Texture
A harsh, high-frequency film grain that feels like a xeroxed club flyer pasted onto a concrete overpass.

```css
body {
  background-color: var(--bg);
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.08'/%3E%3C/svg%3E");
  background-blend-mode: overlay;
}
```

### Layout character
- **Brutalist Margins**: Extreme, asymmetrical padding (e.g., `padding: 8vw 2vw 2vw 12vw;`) that creates deliberate tension.
- **Harsh Borders**: 1px solid `var(--line)` framing all structural containers, making the grid visibly exposed rather than hidden.
- **Scale Contrast**: Typographic scales jump abruptly from `14px` monospace body text to `8rem` display headings with no middle ground.
- **Negative Space**: Vast, empty black voids that force the user to scroll through silence before hitting dense blocks of information.

### Motion character
- **Easing**: `CustomEase.create("snap", "M0,0 C0.1,1 0,1 1,1")` | Duration: `0.3s`.
- Strobe-like and immediate. No soft fades. Elements reveal via harsh CSS `clip-path: polygon()` wipes.
- Hover states are instant binary flips (black text on acid yellow background) with no transition duration.

### Icons
- **Style**: 1.5px stroke, harsh square terminals (no `linecap="round"`), sharp 90-degree angles. Purely geometric and schematic, looking more like architectural blueprints than UI metaphors.

---

## 7. 孟买 (Mumbai)

**Emotional register**: Thick, golden humidity wraps around you, carrying the scent of marigolds, exhaust, and sea salt. It's a beautiful collision of eras where crumbling, pastel Art Deco cinemas stand shoulder-to-shoulder with glittering glass towers, creating a relentless, vibrant sensory overload.

### Fonts
- **Display**: `Roslindale Display` — A lush, high-contrast serif that captures Bombay's fading Art Deco architectural heritage with a sharp contemporary edge.
- **Body**: `Darker Grotesque` — A slightly quirky, warm sans-serif that sits densely on the page while maintaining excellent legibility.
- *Accent note*: Use sweeping italics for introductory paragraphs to add a lyrical, cinematic quality.

### Colors
```css
--line:         rgba(45, 22, 24, 0.15)
```

### Texture
A warm, fibrous paper grain layered under a subtle watercolor-like wash, evoking painted plaster aging in the monsoon.

```css
body {
  background:
    linear-gradient(135deg, var(--bg) 0%, rgba(242, 197, 161, 0.15) 100%),
    url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.04' numOctaves='2' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.06'/%3E%3C/svg%3E");
}
```

### Layout character
- **Z-Index Layering**: Overlapping UI elements (images overlapping text cards overlapping background motifs) to mimic the city's extreme architectural and cultural density.
- **Framed Containers**: Use of subtle double-borders or inset rounded corners (`border-radius: 12px 12px 0 0`) reminiscent of local Deco arches.
- **Maximalist Color Blocking**: Secondary sections switch entirely to the Vermilion or Terracotta backgrounds to create overwhelming, rich shifts in mood.
- **Bleeding Assets**: Images break out of their containers, cropping unpredictably like posters layered over one another on a street wall.

### Motion character
- **Easing**: `Power3.easeInOut` | Duration: `0.9s - 1.2s`.
- Fluid, sweeping, and lingering.
- Elements stagger into view with a slight parallax, like pushing through a crowded, vibrant market. Heavy use of slow, continuous panning on background images.

### Icons
- **Style**: 2px stroke, rounded caps. Slightly ornate with misregistered fill colors (the solid background color of the icon sits 3px off-center from the stroke, mimicking vintage offset Bollywood poster printing).

---

## 8. 香港 (Hong Kong)

**Emotional register**: Looking up through a dizzying canyon of towering, rain-slicked residential blocks as the glow of a red neon pawn-shop sign bleeds into the fog. It is a state of perpetual, hyper-dense kinetic motion where ancient tradition is compressed into a futuristic grid.

### Fonts
- **Display**: `GT America Compressed` — Extremely narrow and vertical. It forces the eye upward, mimicking the suffocating but awe-inspiring skyline.
- **Body**: `IBM Plex Sans` — Technical, global, and highly functional, perfectly suited to handle parallel East-meets-West multilingual typesetting.
- *Accent note*: Chinese typography (e.g., `Noto Sans HK`) should be weight-matched and occasionally run in vertical writing modes for striking structural contrast.

### Colors
```css
--line:         rgba(255, 46, 76, 0.25)
```

### Texture
A subtle CRT scanline effect layered over a deep radial gradient, evoking neon light diffusing through dense atmospheric grime and rain.

```css
body {
  background:
    repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(230,244,241,0.02) 2px, rgba(230,244,241,0.02) 4px),
    radial-gradient(circle at 50% -20%, var(--bg-surface), var(--bg) 80%);
  background-attachment: fixed;
}
```

### Layout character
- **Extreme Verticality**: Narrow, multi-column layouts. Content blocks are taller than they are wide.
- **Ticker-Tape Marquees**: Continuous horizontal scrolling text bands running behind or across structural elements, evoking the constant flow of commerce and traffic.
- **Bilingual Density**: English and Traditional Chinese text locking up together in tight grids, treating the typographic pairing as a dense UI texture.
- **Glowing Hierarchy**: Instead of standard drop shadows, elevated elements use colored, spread out `box-shadow` (e.g., `box-shadow: 0 0 20px rgba(255, 46, 76, 0.15)`) to create a humid, neon-bleed effect.

### Motion character
- **Easing**: `Expo.easeInOut` | Duration: `0.5s - 0.7s`.
- Nervous, kinetic, and high-speed.
- Animations have a slight elastic "bounce" or glitch effect on hover. Marquees never stop moving. Scroll-jacking is used to accelerate the vertical translation of background images, amplifying the feeling of falling upward.

### Icons
- **Style**: 1px stroke, sharp intersections. High-tech and cybernetic. When active, icons gain a subtle chromatic aberration effect (a faint red drop shadow shifted left, a faint cyan shadow shifted right).

Here is the design system documentation for Lisbon, Havana, and Dubai. As a creative director, my goal here is to push past the typical tourism tropes and capture the *visceral, atmospheric* truth of these places using precise typographic, chromatic, and motion cues.

---

## 9. 里斯本 (Lisbon)

**Emotional register**: A city steeped in *saudade*—a profound, beautiful melancholy. The air feels heavy with ocean salt, and the light reflects off worn, pastel ceramic facades that are infinitely more romantic because they are slowly surrendering to time and the Atlantic wind.

### Fonts
- **Display**: `Ogg` — A sweeping, calligraphic serif that feels deeply romantic, slightly weeping in its italics, capturing the maritime poetry of the city.
- **Body**: `PP Neue Montreal` — Clean, unpretentious, providing a modern structural anchor to the highly emotive display type.
- *Accent note*: Use `Instrument Serif` in all-lowercase italic for intimate, poetic micro-copy (14px, tracked tightly).

### Colors
```
--line:         rgba(26, 43, 58, 0.12)
```

### Texture
A subtle, chalky grain that mimics the tactile friction of sea salt on a glazed ceramic tile.

```css
background-color: var(--bg);
background-image:
  radial-gradient(circle at 50% 0%, rgba(200,90,71,0.04) 0%, transparent 60%),
  url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='0.06'/%3E%3C/svg%3E");
```

### Layout character
- **Fluid & Topographical**: Break out of rigid columns. Modules should overlap and stagger vertically, mimicking the experience of walking up the steep, winding, unpredictable hills of the Bairro Alto.
- **Tiled Framing**: Use 1px borders (`--line`) to create a mosaic-like underlying grid. Images shouldn't bleed to the edges; they should sit inside padded "tiles".
- **Generous "Light"**: Extreme padding (120px+) around major typographic elements to let the warm background color breathe, simulating the famous bright Lisbon sunlight.
- **Soft Corners**: Border-radius set to a gentle `4px`—nothing aggressively sharp, mimicking weather-worn stone.

### Motion character
- `power2.inOut` (Duration: `1.4s - 2.0s`)
- **Drifting Fades**: Elements shouldn't snap; they should drift into place like a gentle sea fog rolling in.
- **Tidal Reveals**: Mask reveals should consistently move bottom-to-top, slow and deliberate, evoking rising water.
- **Soft Parallax**: Background images should move at a significantly slower rate than the scroll, emphasizing depth and a slower pace of life.

### Icons
- 1.25px stroke, rounded linecaps and joins. They should feel slightly organic, reminiscent of the intricate, hand-wrought iron balconies found throughout the city. No sharp geometric angles.

---

## 10. 哈瓦那 (Havana)

**Emotional register**: A sticky, intoxicating time capsule dripping with humidity. Heavy Detroit chrome glints under a relentless tropical sun, while peeling, multi-layered colonial walls serve as the canvas for faded, hand-painted revolution-era typography.

### Fonts
- **Display**: `Champion Gothic` — Heavy, uncompromising, and industrial. It carries the weight of 1950s American automotive engineering and block-printed street posters.
- **Body**: `Courier Prime` — A monospace anchor that brings a bureaucratic, typewriter-era authenticity.
- *Accent note*: A sign-painter script (`Dancing Script` or `Pacifico` on Google Fonts) adds vintage contrast as a decorative layer — effective on background watermarks, section ornaments, or pull quotes. **Never apply script fonts to buttons or nav items** — legibility collapses at interactive element sizes.

### Colors
```
--line:         rgba(42, 30, 25, 0.25)
```

### Texture
Thick, gritty, and humid. It needs to look like a wall that has been painted over six times since 1958, with the bottom layers bleeding through.

```css
background-color: var(--bg);
background-image:
  linear-gradient(180deg, rgba(135,179,176,0.15) 0%, transparent 40%),
  linear-gradient(45deg, rgba(230,90,75,0.08) 0%, transparent 100%),
  url("data:image/svg+xml,%3Csvg viewBox='0 0 400 400' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.4' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.15' mix-blend-mode='color-burn'/%3E%3C/svg%3E");
```

### Layout character
- **Posterized & Modular**: Layouts should feel like a wall of wheat-pasted posters. Heavy use of thick borders (`2px solid var(--ink)`) separating content blocks.
- **Raw Edges**: Images should be high-contrast and slightly desaturated, with no border radius (0px). Absolute brutalist framing.
- **Typographic Dominance**: Display text should be massive, set in uppercase, with extremely tight line-height (`0.85`), forcing the words to feel like heavy machinery packed tightly together.
- **Overlap & Bleed**: Text should occasionally break out of its containing boxes or overlap onto images, mimicking the chaotic energy of the streets.

### Motion character
- `back.out(1.5)` (Duration: `0.6s - 0.8s`)
- **Mechanical & Snappy**: Animations should feel heavy and decisive, like a heavy car door slamming shut or a mechanical typewriter striking paper.
- **Staggered Impact**: Lists and nav items should drop in with a rigid stagger (`0.05s`), creating a staccato rhythm.
- **Hover States**: Instead of smooth color transitions, use harsh, instant invert effects (swapping `--bg` and `--ink`) on hover.

### Icons
- 2px to 2.5px heavy stroke, square linecaps. Completely solid and brutalist. They should look like they were applied with a slightly worn rubber stamp.

---

## 11. 迪拜 (Dubai)

**Emotional register**: Audacious scale and hyper-luxury achieved through artificial perfection. A mirage of flawless glass and brushed metal rising from the desert. It is intimidating, mathematically precise, and undeniably expensive—devoid of organic grit, completely mastered by design.

### Fonts
- **Display**: `Monument Extended` — Ultra-wide, architectural, and imposing. It demands space and feels like reading the facade of a megastructure.
- **Body**: `Neue Haas Grotesk` (or `Inter`) — The epitome of invisible, flawless Swiss perfection. No quirks, just pure information delivery.
- *Accent note*: Use extreme tracking (letter-spacing: `0.15em` to `0.2em`) on small, all-caps subheaders to amplify the feeling of vast horizontal space.

### Colors
```
--line:         rgba(227, 194, 152, 0.20)
```

### Texture
Zero noise. Absolutely frictionless. The background uses a subtle architectural blueprint grid combined with a glassy, anisotropic light sheer.

```css
background-color: var(--bg);
background-image:
  linear-gradient(135deg, rgba(255,255,255,0.02) 0%, transparent 40%),
  linear-gradient(to right, rgba(227,194,152,0.03) 1px, transparent 1px),
  linear-gradient(to bottom, rgba(227,194,152,0.03) 1px, transparent 1px);
```

### Layout character
- **Intimidating Negative Space**: Push margins to the absolute extreme. If you think there's enough empty space, double it. Everything must feel vast.
- **Extreme Scale Contrast**: Pair massive `Monument Extended` headlines (120px+) with tiny, meticulously tracked-out micro-copy (10px). The contrast emphasizes the scale of the skyscrapers vs. the human on the ground.
- **Flawless Symmetry & Axes**: Elements must align to a strict mathematical grid. Center-aligned hero sections with perfectly balanced asymmetrical counter-weights as you scroll.
- **Glassmorphism Done Right**: Use `backdrop-filter: blur(24px)` on deeply transparent surface panels (`rgba(18, 18, 20, 0.6)`) bordered by a 1px `--line` to simulate high-end architectural glass.

### Motion character
- `expo.inOut` (Duration: `1.8s - 2.5s`)
- **Frictionless Gliding**: Movement should be exceptionally smooth and mathematically precise. Elements slide on strict X and Y axes.
- **Scale reveals**: Images scaling down from `1.2` to `1.0` inside hidden overflows over a long duration, simulating the smooth ascent of a high-speed glass elevator.
- **Luminance fades**: Text doesn't just fade in via opacity; use CSS clipping and subtle blur filters that transition from `blur(10px)` to `blur(0px)` so text "focuses" into perfect clarity.

### Icons
- 0.75px hairline stroke, perfectly sharp edges. Flawless geometry based on circles and squares. They should look like highly technical architectural blueprint markings rather than UI elements.

Here is the complete design system for the three cities, crafted with distinct, uncompromising visual identities.

---

## 12. 马拉喀什 (Marrakech)

**Emotional register**: A sensory labyrinth baking in the afternoon heat, thick with the scent of crushed spices and oud wood. It is a space of intimate, shaded courtyards hidden behind dense, sun-drenched terracotta walls, where sudden bursts of saturated jewel tones interrupt the dust.

### Fonts
- **Display**: `Ogg` — A lush, calligraphic serif with flowing ligatures that mimic the fluid, rhythmic strokes of Arabic script without being literal.
- **Body**: `Satoshi` — A warm, highly legible geometric sans-serif that grounds the opulent display type with quiet modernism.
- *Accent note*: Use tightly tracked uppercase `Satoshi` in `--accent` (Majorelle Blue) for subheadings to cut through the warmth.

### Colors
```css
--line:         rgba(45, 30, 22, 0.12)
```

### Texture
A subtle, repeating geometric diamond mesh that evokes traditional Zellige tilework, applied via a low-opacity CSS gradient to feel like a watermark on plaster.

```css
background-color: var(--bg);
background-image:
  linear-gradient(135deg, transparent 48%, var(--line) 49%, var(--line) 51%, transparent 52%),
  linear-gradient(45deg, transparent 48%, var(--line) 49%, var(--line) 51%, transparent 52%);
background-size: 48px 48px;
```

### Layout character
- **Labyrinthine & Layered**: Elements overlap heavily. Text boxes bleed into image containers, forcing the user's eye to wander and discover rather than scroll linearly.
- **Framed Densities**: Heavy use of inner borders (`1px solid var(--line)`) with tight `12px` padding to create "courtyards" of content within the larger page.
- **Asymmetric Balance**: Two-column grids where one column is 30% width and locked, while the other is 70% and scrolls, mirroring the narrow, winding alleys of the souk.
- **Maximalist Margins**: Surprising lack of negative space; the canvas feels dense, rich, and intentionally overwhelming.

### Motion character
- **GSAP Ease**: `power2.inOut`
- **Duration**: `1.2s - 1.8s`
- **Style**:
  - Languid and fluid, like heat rising from the pavement.
  - Staggered reveals (`stagger: 0.15`) on typography to make words cascade into view organically.
  - Images scale up from `1.1` to `1.0` inside hidden overflows over a long duration, feeling like stepping out of a dark alley into a bright courtyard.

### Icons
- **Style**: 1.5px stroke, contrasting thick-and-thin lines if possible.
- **Geometry**: Sharp outer corners with rounded, sweeping inner curves (mimicking the iconic Moorish keyhole arch).
- **Personality**: Ornate but sharply scaled, never completely symmetrical.

---

## 13. 斯德哥尔摩 (Stockholm)

**Emotional register**: The immaculate, quiet clarity of a Baltic winter morning. It is an exercise in extreme Nordic restraint, where the pale light reveals functionalism as the purest form of beauty, and warmth is found in the meticulous perfection of raw materials.

### Fonts
- **Display**: `Monument Grotesk` — Highly engineered, coldly beautiful, and utilitarian. Set with `-0.03em` tracking.
- **Body**: `Aeonik` — A pure, structural neo-grotesque that renders perfectly crisp at small sizes (13px - 14px).
- *Accent note*: Use italics in `Aeonik` exclusively for functional labels (e.g., *Fig. 1*, *Read more*).

### Colors
```css
--line:         rgba(26, 27, 28, 0.08)
```

### Texture
A barely perceptible SVG micro-grain noise that mimics the matte, anti-reflective finish of high-end Scandinavian industrial design.

```css
background-color: var(--bg);
background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='0.03'/%3E%3C/svg%3E");
```

### Layout character
- **Extreme Grid Adherence**: An absolute, unbreakable 12-column grid. Everything aligns mathematically to the baseline and column edges.
- **Massive Negative Space**: `12vw` margins on the container. The empty space is treated as the primary design element, holding the content in suspension.
- **Typographic Hierarchy via Spacing**: Instead of using multiple font sizes, hierarchy is established through extreme indentation and white space.
- **Flush Left, Ragged Right**: Absolute refusal to center text. Everything anchors to the left, reinforcing stability and purpose.

### Motion character
- **GSAP Ease**: `expo.out`
- **Duration**: `0.6s - 0.8s`
- **Style**:
  - Snappy, frictionless, and precise. No bounce, no elasticity.
  - Elements slide along the Y-axis by exactly `24px` while fading in from `0`.
  - Hover states are instant (0.1s) and functional, often just an underline appearing or a subtle shift to `--accent`.

### Icons
- **Style**: 1.2px constant stroke weight, butt caps (flat ends), sharp miters.
- **Geometry**: Constructed entirely from perfect circles, squares, and straight lines. No organic curves.
- **Personality**: Clinical, diagrammatic, and deeply reliable. They should look like architectural blueprints.

---

## 14. 布宜诺斯艾利斯 (Buenos Aires)

**Emotional register**: Melancholic grandeur dripping with tropical humidity. It is the faded elegance of a decaying Parisian facade met with the sharp, syncopated tension of a midnight tango—a city suspended between Old World glory and raw, passionate grit.

### Fonts
- **Display**: `GT Alpina` — A sharp, idiosyncratic serif that feels intensely historical but slightly twisted and bookish. Beautiful in grand, oversized italic styles.
- **Body**: `Chivo` — A sturdy, robust grotesque (designed by an Argentine foundry) that anchors the poetic display type with working-class grit.
- *Accent note*: Heavy, dramatic capitalization mixed with tiny superscript notations for an editorial, literary feel.

### Colors
```css
--line:         rgba(26, 17, 13, 0.25)
```

### Texture
Vertical, weeping linear gradients that simulate humidity stains and time-worn aging on a grand European-style stucco wall.

```css
background-color: var(--bg);
background-image:
  linear-gradient(to bottom, rgba(26,17,13,0) 0%, rgba(26,17,13,0.04) 50%, rgba(26,17,13,0) 100%),
  linear-gradient(to right, rgba(155,34,38,0.02) 0%, transparent 5%, transparent 95%, rgba(155,34,38,0.02) 100%);
background-size: 100% 160px, 60px 100%;
```

### Layout character
- **Cinematic & Centralized**: Dramatic, stage-like framing. Content often sits dead-center in narrow, elegant columns (`max-width: 45ch`) flanked by generous, moody borders.
- **Scale Tension**: Extreme typographic contrast. A massive, screen-filling `--accent` red italic letter sits right next to a tiny 11px uppercase caption.
- **Beautiful Decay**: Images are slightly misaligned vertically. Blocks of text deliberately break out of `--bg-surface` containers to overlap the background, mimicking architectural ruin.
- **Thematic Color Inversion**: Frequent, stark sections that flip entirely to `--bg-surface` (Midnight) and `--accent` (Oxblood) to simulate stepping into a dim tango hall from the street.

### Motion character
- **GSAP Ease**: `circ.inOut` mixed with `back.out(1.2)`
- **Duration**: `1.0s - 1.5s`
- **Style**:
  - Syncopated rhythm. Animations hold for a fraction of a second too long, then snap into place, mirroring the deliberate, tense pauses in a tango step.
  - Image hovers employ a slow pan/zoom combined with a CSS `grayscale(100%)` to `grayscale(0%)` filter transition to evoke memories coming to life.

### Icons
- **Style**: 1.5px stroke, teardrop terminals, and ornamental flourishes.
- **Geometry**: Art Nouveau inspired—tall, elongated forms with elegant, asymmetrical whiplash curves.
- **Personality**: Glamorous, slightly theatrical, and dripping with nostalgia.

---

## 15. 墨西哥城 (Mexico City)

**Emotional register**: Geometric brutalism meets saturated pop. Silence and heat. Architecture as art.

### Fonts
- **Display**: `Clash Display` or `Monument Extended` — ultra-bold, all-caps, oppressive scale
- **Body**: `Inter` — clean geometric sans

### Colors
```
--bg:           #F5F5F0    /* stucco white */
--bg-surface:   #EDEDE8
--ink:          #101010    /* near black */
--ink-muted:    #555550
--accent:       #F20587    /* Barragán pink */
--accent-soft:  #FFC000    /* marigold */
--line:         rgba(16,16,16,0.12)
```

### Texture
Hard shadows at 45 degrees, no blur. Flat solid color blocks collide directly. Rough plaster noise at 3% opacity.

```css
background-color: var(--bg);
background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='150' height='150'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.75' numOctaves='4' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='150' height='150' filter='url(%23n)' opacity='0.03'/%3E%3C/svg%3E");
```

### Layout character
- **Brutal geometry**: Large solid-color panels slam into each other with no gradient transitions
- **Hard drop shadows**: `box-shadow: 8px 8px 0 var(--ink)` — zero blur, pure offset
- **Type as architecture**: Headlines set in all-caps ultra-bold at 80–120px, acting as structural walls
- **Accent punch**: A single `--accent` pink element dominates each section — never diluted

### Motion character
- **GSAP Ease**: `power4.out` — snaps fast, like a door slamming
- **Duration**: `0.4s–0.7s`
- **Style**: Elements enter from extreme positions (off-screen by 120px) and lock into place without bounce

### Icons
- **Style**: 2px stroke, perfectly sharp 90-degree corners, no round linecaps
- **Geometry**: Constructivist — squares, triangles, bold diagonals
- **Personality**: Graphic, confrontational, poster-art energy

---

## 16. 雷克雅未克 (Reykjavik)

**Emotional register**: Arctic clarity. Glacial silence. The uncanny beauty of a world with no humans.

### Fonts
- **Display**: `Space Grotesk` or `Syncopate` — wide tracking, industrial micro-cuts
- **Body**: `Space Grotesk` light weight, letter-spacing: 0.05em

### Colors
```
--bg:           #121417    /* basalt black */
--bg-surface:   #1C2028
--ink:          #F0F4F8    /* glacier white */
--ink-muted:    #8A9BB0
--accent:       #00FF9D    /* aurora neon — use sparingly */
--accent-soft:  #B8D8D8    /* frozen cyan */
--line:         rgba(240,244,248,0.08)
```

### Texture
Film grain overlay + glassmorphism. Cold-toned. Micro-bright edge highlights simulate ice-surface refraction.

```css
background-color: var(--bg);
background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='4' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='200' height='200' filter='url(%23n)' opacity='0.05'/%3E%3C/svg%3E");
```

### Layout character
- **Extreme negative space**: 40–50% of sections are empty, enforcing glacial calm
- **Wide tracking everywhere**: All text `letter-spacing: 0.08em–0.15em`
- **Glassmorphism cards**: `backdrop-filter: blur(24px)`, `background: rgba(28,32,40,0.6)`, 1px frost border
- **Accent sparingly**: `--accent` neon green appears only at interaction moments (button glow, active state)

### Motion character
- **GSAP Ease**: `expo.out` — imperceptibly slow start, then sudden arrival
- **Duration**: `1.0s–1.6s`
- **Style**: Elements materialize from opacity 0 at exact position — no movement, just emergence, like ice forming

### Icons
- **Style**: 1px stroke, squared terminals, futuristic cuts
- **Geometry**: Technical — circuit-board-adjacent, minimal nodes and connectors
- **Personality**: Cold, precise, inhuman in the best way

---

## 17. 新加坡 (Singapore)

**Emotional register**: Solarpunk optimism. Nature and technology at peace. The future that actually got built.

### Fonts
- **Display**: `Plus Jakarta Sans` bold — rounded, friendly, confident
- **Body**: `Plus Jakarta Sans` or `Roobert` regular

### Colors
```
--bg:           #E8F2F6    /* canopy glass */
--bg-surface:   #FFFFFF
--ink:          #1B262C    /* titanium */
--ink-muted:    #4A6470
--accent:       #00D26A    /* bio green */
--accent-soft:  #7B2CBF    /* orchid violet */
--line:         rgba(27,38,44,0.1)
```

### Texture
Glossy tropical leaf sheen. Transparent acrylic layers. Soft diffuse shadows with no hard edges.

```css
background-color: var(--bg);
background-image:
  radial-gradient(ellipse at 20% 50%, rgba(0,210,106,0.07) 0%, transparent 60%),
  radial-gradient(ellipse at 80% 20%, rgba(123,44,191,0.05) 0%, transparent 50%);
```

### Layout character
- **Airy grid**: Generous padding, everything breathes — `padding: 7rem 6vw`
- **Rounded everything**: `border-radius: 20px–32px` on cards, buttons, panels
- **Soft elevation**: Cards use `box-shadow: 0 8px 40px rgba(27,38,44,0.08)` — no hard lines
- **Green data accents**: Statistics and metrics highlighted in `--accent` green, evoking growth

### Motion character
- **GSAP Ease**: `power2.out` — organic, breath-like
- **Duration**: `0.7s–1.0s`
- **Style**: Elements rise gently from 20px below. Hover states feel alive, like leaves adjusting to wind.

### Icons
- **Style**: 2px stroke, round linecaps, rounded corners
- **Geometry**: Organic — leaf shapes, flowing lines, botanical references
- **Personality**: Warm, optimistic, approachable tech-forward

---

## 18. 圣托里尼 (Santorini)

**Emotional register**: Blinding whiteness and impossible blue. Time dissolves here. Pure sensation.

### Fonts
- **Display**: `Ogg` or `Playfair Display` — high-contrast serif, elegant with optional italic
- **Body**: `Montserrat` thin or light

### Colors
```
--bg:           #FDFDFD    /* blinding lime-white */
--bg-surface:   #F5F0EC    /* warm stone */
--ink:          #004B87    /* Aegean blue */
--ink-muted:    #6B8BAA
--accent:       #D92568    /* bougainvillea */
--accent-soft:  #DCD0C0    /* warm stone */
--line:         rgba(0,75,135,0.12)
```

### Texture
SVG wave dividers everywhere. Large border radii. Pure white panels with subtle warm-stone shadows.

```css
background-color: var(--bg);
background-image:
  radial-gradient(ellipse at 50% 100%, rgba(0,75,135,0.06) 0%, transparent 60%);
```

### Layout character
- **Wave section dividers**: Every section ends with a gentle SVG wave, never a straight line
- **Organic curves**: `border-radius: 24px–48px` universally — no sharp corners anywhere
- **Blue/white polarity**: Sections alternate between blinding white and deep Aegean, creating rhythm
- **Oversized serif**: Display type set at massive scale, tilted slightly (-2deg), overlapping imagery

### Motion character
- **GSAP Ease**: `sine.inOut` — wave-like oscillation
- **Duration**: `0.9s–1.3s`
- **Style**: Elements drift in on a gentle diagonal path, like paper carried by sea breeze

### Icons
- **Style**: 1.5px stroke, perfectly round terminals, graceful curves
- **Geometry**: Mediterranean — compass roses, wave motifs, arch shapes
- **Personality**: Romantic, sun-bleached, unhurried

---

## 19. 拉各斯 (Lagos)

**Emotional register**: Voltage. A city that never stops moving. Every surface is a canvas.

### Fonts
- **Display**: `Syne` ExtraBold or a variable font with width axis — stretched, distorted, alive
- **Body**: `Syne` or `DM Sans`

### Colors
```
--bg:           #101820    /* deep indigo */
--bg-surface:   #1A2535
--ink:          #E5FF00    /* voltage yellow */
--ink-muted:    #8899AA
--accent:       #FF3B00    /* Lagos red */
--accent-soft:  #00E5FF    /* cyber cyan */
--line:         rgba(229,255,0,0.15)
```

### Texture
Halftone dot screens. Motion blur streaks. High-contrast vector geometric masks layered over photography.

```css
background-color: var(--bg);
background-image:
  radial-gradient(circle at 10% 20%, rgba(255,59,0,0.12) 0%, transparent 40%),
  radial-gradient(circle at 90% 80%, rgba(0,229,255,0.08) 0%, transparent 40%),
  url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='20' height='20'%3E%3Ccircle cx='2' cy='2' r='1' fill='rgba(229,255,0,0.06)'/%3E%3C/svg%3E");
background-size: 100% 100%, 100% 100%, 20px 20px;
```

### Layout character
- **Type as graphic element**: Headlines set at 100–160px, overflow the screen, act as background texture
- **Diagonal cuts**: Sections use `clip-path: polygon(0 0, 100% 5%, 100% 95%, 0 100%)` for kinetic energy
- **Marquee text strips**: Scrolling horizontal text bands between sections
- **Color collision**: `--ink` yellow, `--accent` red, and `--accent-soft` cyan all appear in the same section

### Motion character
- **GSAP Ease**: `elastic.out(1, 0.5)` — overshoots and bounces
- **Duration**: `0.5s–0.8s` — fast, relentless
- **Style**: Elements glitch into position. Stagger is tight (0.04s). The whole page feels like it's about to explode.

### Icons
- **Style**: 2px stroke, sharp angled terminals, occasional filled shapes
- **Geometry**: Graphic — bold Afrocentric geometric patterns, concentric shapes, tribal-derived abstract marks
- **Personality**: Loud, confident, unapologetically alive

---

## 20. 棕榈泉 (Palm Springs)

**Emotional register**: Postwar optimism crystallized. Atomic age confidence. The Sunday afternoon that never ends.

### Fonts
- **Display**: `Futura` or `GT Walsheim` — pure geometric sans from the atomic era
- **Body**: `GT Walsheim` or `DM Sans`
- **Accent**: One retro script font (`Pacifico`) for a single headline or section label — used once, memorably

### Colors
```
--bg:           #F4EBD9    /* desert sand */
--bg-surface:   #FFF8F0
--ink:          #2B2118    /* warm espresso */
--ink-muted:    #7A6552
--accent:       #4DE1C1    /* pool aqua */
--accent-soft:  #FF8A8A    /* flamingo pink */
--line:         rgba(43,33,24,0.1)
```

### Texture
Terrazzo stone pattern. Matte paper warmth. Retro flat illustration aesthetic — no photorealism.

```css
background-color: var(--bg);
background-image:
  radial-gradient(circle at 20% 30%, rgba(77,225,193,0.08) 0%, transparent 30%),
  radial-gradient(circle at 80% 70%, rgba(255,138,138,0.08) 0%, transparent 30%),
  url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='80' height='80'%3E%3Ccircle cx='15' cy='15' r='3' fill='rgba(77,225,193,0.08)'/%3E%3Ccircle cx='55' cy='45' r='2' fill='rgba(255,138,138,0.07)'/%3E%3Ccircle cx='40' cy='70' r='4' fill='rgba(43,33,24,0.04)'/%3E%3C/svg%3E");
background-size: 100% 100%, 100% 100%, 80px 80px;
```

### Layout character
- **Kidney curves**: Section dividers and card shapes use organic, kidney/amoeba outlines via SVG `clip-path`
- **Warm neutrals dominate**: `--bg` and `--bg-surface` carry most sections; accents are bright surprises
- **Retro illustration panels**: Feature sections use flat vector illustrations (no icons — full scenes)
- **Sunburst motifs**: Radial line patterns used as decorative dividers

### Motion character
- **GSAP Ease**: `back.out(1.4)` — a little overshoot, like a spring toy
- **Duration**: `0.6s–0.9s`
- **Style**: Cheerful entry animations. Elements pop in with slight scale overshoot. Hover has a playful lift.

### Icons
- **Style**: 2px stroke, round everything, filled accent dots
- **Geometry**: Retro atomic — starbursts, amoeba blobs, kidney shapes, rocket fins
- **Personality**: Playful, mid-century charming, nostalgic but not kitschy

---

## 21. 伊斯坦布尔 (Istanbul)

**Emotional register**: 跨越亚欧大陆的繁华与神秘，带有复古香料的温暖与拜占庭式的华丽感，古老却充满生命力。

### Fonts
- **Display**: `Playfair Display` — 拥有极高的对比度与优雅的字重，如同精雕细琢的古典清真寺尖塔。
- **Body**: `Work Sans`

### Colors
```
--bg:           #2A1B18    /* 浓郁的土耳其黑咖啡色 */
--bg-surface:   #3E2723
--ink:          #F5E6D3    /* 羊皮纸般的复古暖白 */
--ink-muted:    #BCAAA4
--accent:       #D84315    /* 充满感官刺激的藏红花/香料红 */
--accent-soft:  #FFCCBC
--line:         rgba(216, 67, 21, 0.3)
```

### Texture
模拟大巴扎集市上方穿透彩绘玻璃的幽暗散射光晕。

```css
background-image: radial-gradient(circle at 50% 0%, rgba(216, 67, 21, 0.12) 0%, transparent 60%);
```

### Layout character
- 抛弃僵硬的网格，采用不对称的“拼图式”卡片布局，隐喻这座城市层层叠叠的历史遗迹。
- 采用极细的金色/香料色边框作为容器分割线，营造拜占庭式的华丽秩序感。
- 大量使用具有深邃阴影（Drop Shadow）的悬浮层，拉开视觉的纵深。

### Motion character
- 舒缓、如丝绸般平滑的滚动视差效果，带来时间流逝的沉浸感。
- 元素的揭示动画采用从下至上的缓慢淡入，如同香料烟雾般升腾。

### Icons
- 采用极细线条描绘，带有精妙的东方古典弧度与回环细节。

---

## 22. 迈阿密 (Miami)

**Emotional register**: 充满张力的复古未来主义，阳光海滩、装饰艺术（Art Deco）与霓虹夜生活的完美碰撞，性感且极具挑衅性。

### Fonts
- **Display**: `Righteous` — 极具Art Deco与80年代Synthwave风格的几何无衬线体。
- **Body**: `Montserrat`

### Colors
```
--bg:           #0B1021    /* 迈阿密午夜的深邃海蓝色 */
--bg-surface:   #161D36
--ink:          #E0F7FA    /* 刺眼的冰透冷白 */
--ink-muted:    #80DEEA
--accent:       #FF007F    /* 极度张扬的霓虹火烈鸟粉 */
--accent-soft:  #FF80BF
--line:         rgba(255, 0, 127, 0.3)
```

### Texture
强烈的80年代复古电子网格（Synthwave Grid），直接铺满背景带来数字化的迷幻感。

```css
background-image: repeating-linear-gradient(0deg, transparent, transparent 3px, rgba(255,0,127,0.06) 3px, rgba(255,0,127,0.06) 5px);
```

### Layout character
- 极致的居中对齐排版，配合夸张的大字号标题，带来极强的视觉冲击力。
- 按钮和卡片采用尖锐的直角，外加高饱和度的霓虹发光阴影（Glow Effect）。
- 高对比度的色块切割，强迫用户的视觉聚焦。
- 大量使用双色调（Duotone）处理的摄影图像，剔除平庸的真实色彩。

### Motion character
- 带有强力回弹（Spring）的物理动画效果，干脆且极具弹跳感。
- Hover态引发霓虹色频闪或高亮色块的瞬间反转。
- 快速、激进的页面转场，绝不拖泥带水。

### Icons
- 粗犷的实心矢量图标，自带霓虹发光滤镜特效。

---

## 23. 成都 (Chengdu)

**Emotional register**: 慵懒闲适与赛博朋克的奇妙调和，带着竹林的清幽呼吸感与川味红油的火辣刺激，松弛却绝不平淡。

### Fonts
- **Display**: `Outfit` — 圆润、现代、极具亲和力，传达一种不费力的松弛感。
- **Body**: `Noto Sans`

### Colors
```
--bg:           #F6F8F4    /* 宣纸与淡竹叶的清透微绿 */
--bg-surface:   #E8EFE5
--ink:          #1B2A1E    /* 幽深沉静的墨绿色 */
--ink-muted:    #5D7060
--accent:       #E53935    /* 刺破平静的辣椒红/朱砂红 */
--accent-soft:  #FFCDD2
--line:         rgba(27, 42, 30, 0.1)
```

### Texture
极其微妙的噪点纹理，模拟传统宣纸或粗糙的茶馆桌面，带来触觉上的温润感。

```css
background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.04'/%3E%3C/svg%3E");
```

### Layout character
- 极端的“留白”艺术，给所有元素巨大的呼吸空间，排版绝不拥挤。
- 采用大圆角（`border-radius: 24px`甚至更圆）的流体卡片，消除设计中的攻击性。
- 非强制性的视觉引导，允许内容如流水般自由错落分布。

### Motion character
- 慵懒的缓动函数（如 `cubic-bezier(0.25, 0.1, 0.25, 1)`），让元素的移动如同茶杯上升腾的水汽。
- 滚动时带有微微的漂浮延迟感。

### Icons
- 柔软的圆角线框图标，线宽饱满，气质温和。

---

## 24. 哥本哈根 (Copenhagen)

**Emotional register**: 极致的北欧克制与环保主义，注重功能性与严密的逻辑，透出令人安心的温和与Hygee式的质朴。

### Fonts
- **Display**: `Syne` — 在极致几何中带有一丝前卫的艺术感，打破纯功能主义的无聊。
- **Body**: `Inter`

### Colors
```
--bg:           #E3DAC9    /* 燕麦与骨白色，温暖的北欧中性基调 */
--bg-surface:   #F2EBE1
--ink:          #2C3531    /* 深邃且不反光的碳岩灰 */
--ink-muted:    #788580
--accent:       #D1603D    /* 新港(Nyhavn)建筑的经典陶土红 */
--accent-soft:  #E8B8A8
--line:         rgba(44, 53, 49, 0.12)
```

### Texture
纯净的斜向光晕，犹如北欧漫长冬季里珍贵的低角度日照。

```css
background-image: radial-gradient(circle at 100% 100%, rgba(209, 96, 61, 0.06) 0%, transparent 60%);
```

### Layout character
- 严苛的底栏网格系统（Grid System），如同自行车道般井然有序，绝无像素级的偏差。
- 摒弃任何不必要的装饰线与阴影，全部采用扁平色块与清晰的排版层级划分。
- 大量的图片出血（Bleed）设计，辅以极其克制的色彩搭配。
- 零圆角或极小圆角（2px），强调建筑般的结构感。

### Motion character
- 没有花哨的过渡，只有瞬间的状态切换或极快的线性动画。
- 交互反馈直接、确定，充满机械美学与信赖感。

### Icons
- 粗野主义（Brutalist）风格，绝对的几何形状拼合，线条粗壮有力。

---

## 25. 维也纳 (Vienna)

**Emotional register**: 宏大、庄重且充满古典艺术气息，宛如一场在金色大厅奏响的交响乐，拥有惊人的层次感与不朽的华丽。

### Fonts
- **Display**: `Cinzel Decorative` — 极度华丽、充满威严的古典衬线体，如同宫殿的铭文。
- **Body**: `Lora`

### Colors
```
--bg:           #1A110A    /* 深邃的桃花心木色，犹如古董钢琴 */
--bg-surface:   #2E2016
--ink:          #FDFBF7    /* 象牙质感的纯粹白 */
--ink-muted:    #C5B4A3
--accent:       #D4AF37    /* 克林姆特画作中的帝国耀金 */
--accent-soft:  #F3E5AB
--line:         rgba(212, 175, 55, 0.25)
```

### Texture
细腻的竖向条纹肌理，隐喻歌剧院中垂下的厚重天鹅绒幕布。

```css
background-image: repeating-linear-gradient(90deg, transparent, transparent 40px, rgba(212, 175, 55, 0.02) 40px, rgba(212, 175, 55, 0.02) 80px);
```

### Layout character
- 极其考究的绝对对称布局，以中央轴线为核心向两边展开，营造纪念碑式的神圣感。
- 段落两侧留出宛如画廊般的宽阔边距（Margins）。
- 穿插使用精美的细线作为视觉分割，文本间距（Line-height）刻意拉大以彰显优雅。

### Motion character
- 庄重且克制的编排动画，如同音乐指挥棒的起落，每个元素的出现都有明确的先后韵律。
- 背景图缓慢的放大（Scale）与极度的平滑过渡。
- 悬停时带有微妙的金色流光反馈。

### Icons
- 带有衬线特征的精致图标，仿佛是用羽毛笔精心勾勒的古典徽章。

---

## 26. 开普敦 (Cape Town)

**Emotional register**: 狂野、饱满、充满大地与海洋的生命力。它是大自然的壮阔与南非多元文化的视觉交响。

### Fonts
- **Display**: `Space Grotesk` — 略带古怪的现代字体，宽大且不羁，充满探索欲。
- **Body**: `Rubik`

### Colors
```
--bg:           #004D40    /* 桌山脚下深邃的海洋与灌木绿 */
--bg-surface:   #00695C
--ink:          #FFF8E1    /* 被南非烈日漂白的明亮日光色 */
--ink-muted:    #B2DFDB
--accent:       #FFC107    /* 灼热而狂野的非洲暖阳黄 */
--accent-soft:  #FFECB3
--line:         rgba(255, 193, 7, 0.2)
```

### Texture
粗犷的地质噪点，模拟好望角的风化岩石与粗糙的大地肌理。

```css
background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='rock'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='1.5' numOctaves='2' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23rock)' opacity='0.08'/%3E%3C/svg%3E");
```

### Layout character
- 强烈的斜向（Diagonal）切割与错位排版，打破地平线的平静，注入运动感。
- 照片与色块进行具有侵略性的重叠交错。
- 使用超大号、甚至溢出屏幕的Typography设计，展现原始的力量感。
- 饱和度极高的色块作为底层支撑。

### Motion character
- 充满能量的弹射出场与快速的滑动揭示。
- 鼠标滚动时触发强烈的视差位移，让前景与背景疯狂撕扯。

### Icons
- 块面感极强、边缘粗钝的实心填充图标，摒弃一切脆弱的细线。

---

## 27. 波哥大 (Bogotá)

**Emotional register**: 高海拔的魔幻现实主义，红砖建筑的粗犷粗糙与街头涂鸦艺术的叛逆灵魂相互交织。

### Fonts
- **Display**: `Bebas Neue` — 高耸、紧凑，如同贴满墙面的巨型街头海报，视觉声音极大。
- **Body**: `Karla`

### Colors
```
--bg:           #1B1615    /* 潮湿的柏油路与黑夜的底色 */
--bg-surface:   #2C2220    /* 沉郁的拉美红砖色 */
--ink:          #EAE3D9    /* 粗糙画布般的灰白 */
--ink-muted:    #A89F95
--accent:       #50C878    /* 刺破暗夜的哥伦比亚祖母绿 */
--accent-soft:  #A9DFBF
--line:         rgba(80, 200, 120, 0.25)
```

### Texture
带有喷漆感的斜向半调纹理（Halftone/Spray-can vibe），强化街头艺术的粗糙质地。

```css
background-image: repeating-linear-gradient(45deg, transparent, transparent 8px, rgba(80, 200, 120, 0.04) 8px, rgba(80, 200, 120, 0.04) 16px);
```

### Layout character
- 拼贴画（Collage）风格的布局，图片边缘采用不规则裁剪或粗糙的撕裂边缘。
- 文字野蛮地压在图片上方，毫无顾忌地破坏传统排版的整洁。
- 容器带有轻微的随机倾斜角度，拒绝被规矩束缚。

### Motion character
- 悬停（Hover）时触发轻微的故障艺术（Glitch）或色彩分离效果。
- 快速、略带神经质的闪烁转场。

### Icons
- 类似模版喷漆（Stencil）风格，带有断点和粗糙边缘。

---

## 28. 阿姆斯特丹 (Amsterdam)

**Emotional register**: 前卫与秩序的完美平衡，向“风格派”（De Stijl）的几何美学致敬，却又带着运河波光的流动感。

### Fonts
- **Display**: `Oswald` — 瘦长而紧凑，完美契合阿姆斯特丹标志性的狭窄运河房屋。
- **Body**: `IBM Plex Sans`

### Colors
```
--bg:           #0033A0    /* 深邃且极度吸睛的运河钴蓝 */
--bg-surface:   #0047D4
--ink:          #FFFFFF    /* 毫无杂质的纯白 */
--ink-muted:    #99BBFF
--accent:       #FF3814    /* 蒙德里安画笔下的郁金香亮红 */
--accent-soft:  #FF9C8A
--line:         rgba(255, 255, 255, 0.3)
```

### Texture
严谨的几何网格系统，向蒙德里安的格子艺术致敬。

```css
background-image: repeating-linear-gradient(90deg, rgba(255,255,255,0.06) 0, rgba(255,255,255,0.06) 1px, transparent 1px, transparent 60px);
```

### Layout character
- 极致的模块化（Modular）设计，所有的UI元素都被锁死在可见的网格盒子中。
- 使用粗壮的纯白线条作为盒子的真实物理边界。
- 强烈的色彩碰撞，深蓝底色上直接放置亮红与白色的几何色块。
- 完全剔除圆角，坚持绝对的正交矩形。

### Motion character
- 横向抽屉式的滑动交互，犹如推开一扇扇并排的木门。
- 元素按照网格系统进行类似推箱子（Slide puzzle）的严密位移。

### Icons
- 极致简约的几何原点与直线拼合，完全没有多余的修饰曲线。

---

## 29. 贝鲁特 (Beirut)

**Emotional register**: 历经沧桑却依然迷人的地中海明珠，散发着温暖慵懒的阳光与充满韧性的废墟美学，美丽而破碎。

### Fonts
- **Display**: `Prata` — 锋利、优雅、带有古典雕刻感，犹如罗马时期的石柱切面。
- **Body**: `Jost`

### Colors
```
--bg:           #F5EBE1    /* 被地中海阳光烤暖的砂岩色 */
--bg-surface:   #FFF7F0
--ink:          #3A2E2A    /* 深沉的炭灰与橄榄木色 */
--ink-muted:    #8C7C77
--accent:       #008B8B    /* 清透迷人的地中海青色 */
--accent-soft:  #B3E0E0
--line:         rgba(58, 46, 42, 0.1)
```

### Texture
类似古老砂岩或风化灰泥墙面的细微斑驳感。

```css
background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='ruin'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.05' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23ruin)' opacity='0.05'/%3E%3C/svg%3E");
```

### Layout character
- 带有杂志编辑感（Editorial style）的高级排版，图文穿插极具呼吸感。
- 图片与容器刻意保留不对齐的参差感，隐喻城市中历史与现代的断层。
- 大量运用优美的斜体（Italic）作为引言与副标题的视觉点缀。

### Motion character
- 极其轻柔的交叉淡入淡出（Crossfade），仿佛阳光穿透云层的变化。
- 照片在容器内部带有极其缓慢的推拉（Ken Burns Effect）效果。

### Icons
- 优雅的半衬线（Semi-serif）图标，带有微妙的粗细对比，不追求完美的对称。

---

## 30. 波特兰 (Portland)

**Emotional register**: 随性、独立、充满手工匠人精神。扑面而来的是太平洋西北部的阴冷松林气息与美式复古工业风的温暖。

### Fonts
- **Display**: `Rokkitt` — 厚重的粗衬线体（Slab Serif），带有老式打字机与手工印章的拙朴感。
- **Body**: `Chivo`

### Colors
```
--bg:           #252D27    /* 阴雨天的深邃松针绿 */
--bg-surface:   #333C35    /* 湿润的板岩灰 */
--ink:          #E8E2D2    /* 未经漂白的手工棉布白 */
--ink-muted:    #A4A99E
--accent:       #D9534F    /* 伐木工法兰绒衬衫的铁锈红 */
--accent-soft:  #F2B2B0
--line:         rgba(232, 226, 210, 0.15)
```

### Texture
倾斜的编织纹理，让人联想到粗糙的法兰绒面料或是连绵的细雨。

```css
background-image: repeating-linear-gradient(135deg, rgba(217, 83, 79, 0.04) 0px, rgba(217, 83, 79, 0.04) 2px, transparent 2px, transparent 10px);
```

### Layout character
- 重型、敦实的卡片设计，带有明显的粗边框，强调耐用（Utility-first）的工具感。
- 采用复古徽章（Badge/Stamp）样式的标签设计，代替传统的圆角按钮。
- 拒绝过度设计，保持一种DIY的粗糙感，排版紧凑且极具功能性。

### Motion character
- 按钮点击时带有明显的下压（Press）物理反馈，如同按下老式机械开关。
- 没有轻浮的漂浮动画，一切元素的移动都显得扎实、有重量感。

### Icons
- 类似橡皮章刻印的加粗实心图标，线条粗细略有不均，带有手工温度。
