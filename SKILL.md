---
name: citycraft
description: >-
  Create a bold, visually striking landing page — unconventional layouts, GSAP scroll animations,
  SVG elements, clip-path dividers, real depth and layering. Use this skill whenever the user wants
  a landing page, homepage, product page, marketing page, campaign page, event page, or any
  single-page site that needs to impress. Trigger on: 帮我做一个落地页, 做个首页, 产品展示页, 活动页,
  营销页, 官网首页, landing page, product page, promo page, make me a homepage, build a product
  showcase, create a campaign page. Workflow: asks one question about the product, then opens a live
  browser preview of 57 city-inspired visual styles to click-select, lets the user pick
  typography/nav/color tone/hero variant/features variant/page sections interactively, then outputs
  a complete multi-file site (index.html + style.css + main.js + SVG sprite) with real product copy.
---

# Landing Page Builder

## Philosophy

This skill produces landing pages that are **visually audacious** — not the typical nested-container, card-grid, predictable web template. Every output should feel like a deliberate design artifact:

- **布局大胆** — Clip-path dividers instead of horizontal lines. Type bleeding off-screen. Elements breaking out of their grid. Full-viewport headlines.
- **SVG 作为设计核心** — Not decorative sprinkles. SVG paths animate on scroll, icons have personality, background textures from `<feTurbulence>` noise.
- **层次感与深度** — GSAP ScrollTrigger creates genuine spatial depth: sections that overlap and cover the previous one, sticky panels pinned while content slides over them, parallax on separate z-layers.
- **背景质感** — Every section has texture. Never a flat solid background.
- **导航惊喜** — The nav is never a standard horizontal bar.

---

## Bundled Assets (USE THESE — do not reinvent)

This skill comes with pre-built assets. Read and use them directly:

| File | What's in it | When to use |
|------|-------------|-------------|
| `assets/style-preview-template.html` | 57-city style preview cards | Step 2: `sed` fill `__PRODUCT_NAME__` + `__PRODUCT_HEADLINE__`, save as `style-preview.html`, open |
| `assets/options-preview-template.html` | Interactive demos: 3 typography styles, 4 nav styles, 3 color variants | Step 3: `sed` fill city color tokens + product name, save as `options-preview.html`, open |
| `assets/textures.css` | 6 CSS texture classes (`.texture-kyoto`, `.texture-paris`, `.texture-tokyo`, etc.) | Copy the matching class into `style.css` |
| `assets/gsap-snippets.js` | 6 GSAP animation functions (blur entrance, line reveal, parallax, sticky steps, blast menu, magnetic pill) | Copy the relevant functions into `main.js` |
| `assets/clip-paths.css` | 8 clip-path divider classes (`.clip-diagonal-br`, `.clip-parallelogram`, `.clip-arc-bottom`, etc.) | Use at least 2 in `style.css` for section dividers |
| `assets/sections/hero-variants.html` | 3 Hero section templates (全屏铺张/分屏张力/极简下降) | Step 4: pick the variant matching the user's typography preference, copy and adapt |
| `assets/sections/features-variants.html` | 3 Features section templates (大数字/交替展示/时间线) | Step 4: pick based on content type (stats → big number, how-it-works → timeline) |
| `assets/sections/conversion-variants.html` | Pricing table, testimonial wall, power CTA | Step 4: copy relevant section, all use CSS custom properties |
| `references/product-demo-hero.md` | Product demo hero principles + scene design guide | Read when user wants to show product workflow in hero (see Step 3/4) |

**The quality guarantee of this skill comes from using these assets.** They encode specific design decisions that make outputs distinct. Don't describe what to do — copy the code and adapt it.

---

## The Workflow

### Step 1: Understand the Product

Use `AskUserQuestion` to ask:

> "告诉我你的落地页是关于什么的——产品/服务名称，以及一句话介绍。"

Wait for the answer before proceeding.

### Step 2: Generate the Style Preview

Fill in the two placeholders and open the result — do NOT read the template file into context:
- `PRODUCT_NAME` → the product name from Step 1
- `PRODUCT_HEADLINE` → a short punchy phrase (3–5 words) that captures the product's essence

```bash
_SKILL_DIR=$(ls -d ~/.agents/skills/citycraft 2>/dev/null || ls -d ~/.claude/skills/citycraft 2>/dev/null)
PYTHON=$(command -v python3 2>/dev/null || command -v python 2>/dev/null || echo "")
if [ -n "$PYTHON" ]; then
  # Python available (macOS / Linux / WSL / Windows with Python)
  # Pass LANG=en for English-language conversations
  "$PYTHON" "$_SKILL_DIR/assets/scripts/run_preview.py" \
    --template "$_SKILL_DIR/assets/style-preview-template.html" \
    --output   ./style-preview.html \
    --port     17433 \
    --timeout  300 \
    "LANG=zh" \
    "PRODUCT_NAME=ACTUAL_PRODUCT_NAME" \
    "PRODUCT_HEADLINE=ACTUAL_HEADLINE" \
    "RECEIVER_PORT=17433"
else
  # No Python — substitute via sed and open as a local file.
  # The submit button falls back to clipboard copy automatically.
  sed "s/__PRODUCT_NAME__/ACTUAL_PRODUCT_NAME/g; s/__PRODUCT_HEADLINE__/ACTUAL_HEADLINE/g" \
    "$_SKILL_DIR/assets/style-preview-template.html" > ./style-preview.html
  open ./style-preview.html 2>/dev/null || xdg-open ./style-preview.html 2>/dev/null \
    || echo "Open in browser: $(pwd)/style-preview.html"
  echo "Python not found — no live bridge. The submit button will copy the city name to clipboard. Paste it here."
fi
```

Replace `ACTUAL_PRODUCT_NAME` and `ACTUAL_HEADLINE` with the real values from Step 1 in the script arguments.

> **Windows PowerShell (no WSL/Git Bash):** Run `run_preview.ps1` directly — it has the same interface. See `assets/scripts/run_preview.ps1` for usage.

Tell the user: "我在浏览器里打开了57种城市风格的预览卡片，每个都是真实渲染效果。向下滚动可以看到全部——从京都到拉各斯到棕榈泉，再到伊斯坦布尔、迈阿密、成都、哥本哈根、维也纳、开普敦、波哥大、阿姆斯特丹、贝鲁特、波特兰，以及上海、北京、重庆、西安、杭州、深圳夜、敦煌、苏州、拉萨、罗马、布拉格、墨尔本、雅典、卡萨布兰卡、釜山、巴厘岛、多伦多、特拉维夫、华沙、孟买夜，还有新加入的大阪、清迈、米兰、台北、新奥尔良、苏黎世、温哥华。选好之后直接点卡片发送给我；如果本地桥接没有连上，也可以复制城市名告诉我。如果57个城市都不对，直接用自己的语言描述给我也行。"

### Step 3: Open the Interactive Options Preview

The user has chosen their city. Now open the visual options preview so they can *feel* the layout and nav choices instead of reading descriptions.

> **If the user clicked "让 AI 来选" (city = `__AI_CHOOSE__`):** Skip the preview entirely. Instead, look back at the conversation to understand the product's audience, industry, and tone. Then pick the single most fitting city from `references/city-styles.md` and briefly explain why (2–3 sentences). Confirm with the user: "我为你选了 [城市]——[理由]. 继续吗？" Then proceed to Step 3 with that city.

**3a — Get city color tokens (script, not file read)**

Run `get_city_tokens.py` to extract just the 5 color values — do NOT read `city-styles.md` into context:

```bash
_SKILL_DIR=$(ls -d ~/.agents/skills/citycraft 2>/dev/null || ls -d ~/.claude/skills/citycraft 2>/dev/null)
PYTHON=$(command -v python3 2>/dev/null || command -v python 2>/dev/null || echo "")
# Outputs CITY_BG=, CITY_SURFACE=, CITY_INK=, CITY_MUTED=, CITY_ACCENT=
eval $("$PYTHON" "$_SKILL_DIR/assets/scripts/get_city_tokens.py" "ACTUAL_CITY_NAME")
```

Replace `ACTUAL_CITY_NAME` with the city name the user chose (Chinese or English). The script handles both. If the city isn't found, it exits 1 — in that case fall back to reading the `### Colors` section of `references/city-styles.md` manually.

**3b — Generate and open options-preview.html**

Use the `$CITY_*` variables from 3a. Do NOT read the template file into context:

```bash
if [ -n "$PYTHON" ]; then
  # Pass LANG=en for English-language conversations
  "$PYTHON" "$_SKILL_DIR/assets/scripts/run_preview.py" \
    --template "$_SKILL_DIR/assets/options-preview-template.html" \
    --output   ./options-preview.html \
    --port     17432 \
    --timeout  300 \
    "LANG=zh" \
    "PRODUCT_NAME=ACTUAL_PRODUCT_NAME" \
    "PRODUCT_HEADLINE=ACTUAL_HEADLINE" \
    "CITY_NAME=ACTUAL_CITY_NAME" \
    "CITY_BG=$CITY_BG" \
    "CITY_SURFACE=$CITY_SURFACE" \
    "CITY_INK=$CITY_INK" \
    "CITY_MUTED=$CITY_MUTED" \
    "CITY_ACCENT=$CITY_ACCENT" \
    "CITY_DARK_BG=#0e0c09" \
    "CITY_DARK_SURFACE=#1e1b16" \
    "CITY_DARK_INK=#f2ede4" \
    "CITY_DARK_ACCENT=$CITY_ACCENT" \
    "CITY_BRIGHT_BG=#fdf9f2" \
    "CITY_BRIGHT_SURFACE=#fffdf8" \
    "CITY_BRIGHT_INK=#1a1510" \
    "CITY_BRIGHT_ACCENT=$CITY_ACCENT" \
    "RECEIVER_PORT=17432"
else
  sed \
    -e "s/__PRODUCT_NAME__/ACTUAL_PRODUCT_NAME/g" \
    -e "s/__PRODUCT_HEADLINE__/ACTUAL_HEADLINE/g" \
    -e "s/__CITY_NAME__/ACTUAL_CITY_NAME/g" \
    -e "s/__CITY_BG__/$CITY_BG/g" \
    -e "s/__CITY_SURFACE__/$CITY_SURFACE/g" \
    -e "s/__CITY_INK__/$CITY_INK/g" \
    -e "s/__CITY_MUTED__/$CITY_MUTED/g" \
    -e "s/__CITY_ACCENT__/$CITY_ACCENT/g" \
    -e "s/__CITY_DARK_BG__/#0e0c09/g" \
    -e "s/__CITY_DARK_SURFACE__/#1e1b16/g" \
    -e "s/__CITY_DARK_INK__/#f2ede4/g" \
    -e "s/__CITY_DARK_ACCENT__/$CITY_ACCENT/g" \
    -e "s/__CITY_BRIGHT_BG__/#fdf9f2/g" \
    -e "s/__CITY_BRIGHT_SURFACE__/#fffdf8/g" \
    -e "s/__CITY_BRIGHT_INK__/#1a1510/g" \
    -e "s/__CITY_BRIGHT_ACCENT__/$CITY_ACCENT/g" \
    "$_SKILL_DIR/assets/options-preview-template.html" > ./options-preview.html
  open ./options-preview.html 2>/dev/null || xdg-open ./options-preview.html 2>/dev/null \
    || echo "Open in browser: $(pwd)/options-preview.html"
  echo "Python not found — no live bridge. Use the copy button in the preview and paste the result here."
fi
```

The dark variant (`__CITY_DARK_*`) is always the luxury/night treatment — near-black bg, warm light text, same accent. The bright variant is always the fresh/modern treatment — near-white bg, dark text, same accent. The city's identity comes from the base colors and accent, not from the dark/bright shell.

> **Windows PowerShell (no WSL/Git Bash):** Run `run_preview.ps1` directly. See `assets/scripts/run_preview.ps1` for usage.

When the script exits, it prints the result JSON to stdout. If it times out, ask the user to type their choice manually before proceeding.

Tell the user: "在浏览器里打开了一个互动选择页——有排版、导航的实际演示效果，还有三种色调的对比。可以点击全屏菜单看它怎么爆开，把光标移近底部胶囊感受磁性效果。全部选好之后，点底部的「告诉 Agent →」按钮，我会自动收到结果并继续生成；如果本地桥接没有连上，再把复制结果贴给我就可以。"

**If the user chose a non-city description** (scene, era, material, emotion): read `references/imagery-derivation.md` to derive the design token system first, use those derived colors as the `CITY_*` arg values above, then proceed normally.

If the script prints JSON, parse it directly and continue to Step 4 with `city`, `layout`, `nav`, `tone`, `hero`, `features`, and `sections`. If it times out, ask the user to paste their choices manually before proceeding.

### Step 4: Generate the Landing Page

Output into `{product-name}-landing/`:

```
{product-name}-landing/
├── index.html
├── style.css
├── main.js
└── assets/
    └── icons.svg
```

#### 4a — Bash Assembly (do this first, before writing any file)

**The goal is to avoid outputting bundled asset code as model tokens.** Instead, use Bash to copy and pipe the ready-made assets into the output files. Only product-specific content (copy, tokens, overrides) is written by the model.

**Step 1 — Set up directories**

```bash
_SKILL_DIR=$(ls -d ~/.agents/skills/citycraft 2>/dev/null || ls -d ~/.claude/skills/citycraft 2>/dev/null)
_OUT="./{product-name}-landing"
mkdir -p "$_OUT/assets"
```

**Step 2 — Assemble section variants into a staging file**

Plan which variants to use (see table below), then pipe each into a staging file:

```bash
# Replace B / C / PRICING with the user's actual choices
python3 "$_SKILL_DIR/assets/scripts/extract_variant.py" \
  "$_SKILL_DIR/assets/sections/hero-variants.html" B > "$_OUT/_sections.html"
python3 "$_SKILL_DIR/assets/scripts/extract_variant.py" \
  "$_SKILL_DIR/assets/sections/features-variants.html" C >> "$_OUT/_sections.html"
python3 "$_SKILL_DIR/assets/scripts/extract_variant.py" \
  "$_SKILL_DIR/assets/sections/conversion-variants.html" PRICING >> "$_OUT/_sections.html"
python3 "$_SKILL_DIR/assets/scripts/extract_variant.py" \
  "$_SKILL_DIR/assets/sections/conversion-variants.html" CTA >> "$_OUT/_sections.html"
```

For conversion sections use names: `PRICING`, `COMPARE_PRICING`, `TESTIMONIALS`, `BRAND_WALL`, `CTA`, `FAQ_A`, `FAQ_B`.

**Step 3 — Copy bundled CSS utilities into style.css base**

```bash
# Texture: use --texture flag (never read full city-styles.md)
python3 "$_SKILL_DIR/assets/scripts/get_city_tokens.py" "CITY_NAME" --texture > "$_OUT/_texture.css"
# Clip-paths: copy all classes, model picks which to apply via class names
cat "$_SKILL_DIR/assets/clip-paths.css" >> "$_OUT/_texture.css"
```

**Step 4 — Copy GSAP snippets into main.js base**

```bash
cat "$_SKILL_DIR/assets/gsap-snippets.js" > "$_OUT/_gsap-base.js"
```

Now read the three staging files (`_sections.html`, `_texture.css`, `_gsap-base.js`) to understand what's available, then write the final output files.

#### 4b — Section Variant Reference

Common page sequences:
- SaaS tool: Hero D → Features C → Features A → Pricing → FAQ A → CTA
- Agency portfolio: Hero A → Features B → Testimonials → CTA
- Developer tool: Hero B → Features C → Features A → Pricing → FAQ B → CTA
- Luxury product: Hero C → Features B → Testimonials → CTA

| If the user needs... | Use this template | Variant |
|---------------------|-------------------|---------|
| Hero — massive bold statement | 全屏铺张 | A |
| Hero — product visual + headline | 分屏张力 | B |
| Hero — elegant, story-first | 极简下降 | C |
| Hero — product has a workflow to show | 产品演示型 | D (also read `references/product-demo-hero.md`) |
| Hero — typography-led, high-impact | 文字爆炸型 | E |
| Hero — editorial storytelling | 杂志撕裂型 | F |
| Hero — playful product launch | 弹出卡片型 | G |
| Features — data/metrics focus | 大数字 | A |
| Features — product screenshots | 交替展示 | B |
| How it works — step-by-step | 时间线 | C |
| Features — modular story blocks | 本托格子型 | D |
| Features — browseable capability ribbon | 水平滚动卡带型 | E |
| Features — objection handling | 问答展开型 | F |
| Pricing table | 定价表 | PRICING |
| Pricing comparison with toggle | 对比定价表 | COMPARE_PRICING |
| Testimonials | 引言墙 | TESTIMONIALS |
| Trusted brand logos | 品牌墙 | BRAND_WALL |
| Final CTA | 强力CTA区 | CTA |
| FAQ — editorial layout | 编辑排版型 | FAQ_A |
| FAQ — card grid | 全宽焦点型 | FAQ_B |

#### 4c — Write the Output Files

**index.html** — Write with the Write tool. No markdown block, directly to file.
- Document structure: `<html>`, `<head>` (Google Fonts, GSAP CDN, link to style.css + main.js), `<body>`
- Nav HTML matching the selected nav style
- Paste `<style>` blocks and `<section>` HTML from `_sections.html` in page order
- Replace all placeholder copy with real product copy — fit the city aesthetic's tone of voice
- No Lorem Ipsum, no placeholder text

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
```

**style.css** — Write with the Write tool. Structure:
1. `:root` block — full design token system: colors from `$CITY_*` tokens, chosen fonts, spacing scale, radii. This is the only part the model writes from scratch.
2. Paste texture + clip-path CSS from `_texture.css`
3. Nav CSS matching the selected nav style (from `references/nav-catalog.md`)
4. Layout and typography overrides — only what differs from section defaults

`clamp()` for ALL headline font sizes:
- Hero 主标题：`clamp(2.8rem, 7vw, 7rem)` — 铺张型也不超过 7rem
- Section 标题：`clamp(2rem, 4vw, 4rem)`
- 大数字/装饰数字：`clamp(4rem, 10vw, 9rem)`
- 副标题/说明文字：`clamp(1rem, 1.4vw, 1.2rem)`

Do NOT add comments to style.css — they consume tokens and add no value to the output file.

**main.js** — Write with the Write tool. Structure:
1. `gsap.registerPlugin(ScrollTrigger)`
2. Paste the relevant functions from `_gsap-base.js` — required minimum:
   - `initHeroEntrance()` — stagger hero elements in
   - `initParallax()` — at least 2 layers at different speeds
   - Section heading reveals on viewport entry
   - `initStickySteps()` OR `initBlastMenu()` OR `initMagneticPill()` — matching nav/layout
3. Call sequence at bottom; `ScrollTrigger.refresh()` after fonts load

Do NOT add comments to main.js.

**assets/icons.svg** — SVG sprite with `<symbol>` elements. At minimum: logo mark, nav toggle, arrow, checkmark, 2–3 product-relevant feature icons. Icon style must match the city aesthetic's stroke weight and geometry.

After all files are written, delete the staging files:
```bash
rm -f "$_OUT/_sections.html" "$_OUT/_texture.css" "$_OUT/_gsap-base.js"
```

---

## Design Laws (Never Break These)

1. **No `#ffffff` backgrounds.** Not on sections, not on cards. Warm neutrals: `#f5ede0`. Cool: `#edf0ee`. Dark: `#08060f`. Cards get a slight tint, never pure white.
2. **No `#6366f1`.** Color comes from the city style palette.
3. **No rectangular section dividers.** Use a class from `assets/clip-paths.css` — at least 2 sections must have non-rectangular edges.
4. **No generic icons.** Match the city style's stroke weight and geometry.
5. **Two typefaces minimum.** Display/serif for headlines + clean sans for body. From `references/city-styles.md`. Decorative/script accent fonts (when a city style mentions one) go on watermarks, pull quotes, or ornamental elements — **never on buttons, nav, or body copy**.
6. **Nav must surprise.** Use the chosen nav from `references/nav-catalog.md` with its full surprise element implemented.
7. **Use bundled assets.** The texture, GSAP snippets, and clip-paths must come from the skill's asset files — not reimplemented from scratch.
8. **`.line-wrap` CJK fix.** Whenever the page has Chinese or Japanese text and uses `.line-wrap { overflow: hidden }` for line reveal animations, add `padding-top: 0.15em; margin-top: -0.15em;` to prevent CJK ascenders from being clipped at the top.

---

## Reference Files

- `references/city-styles.md` — Exact design parameters (fonts, colors, textures, motion, icons) for each city aesthetic
- `references/nav-catalog.md` — 4 nav styles with full implementation notes and GSAP code
- `references/imagery-derivation.md` — How to translate any non-city description (scene, era, material, emotion) into a concrete design token system. Read this whenever the user describes something that isn't one of the 57 city cards.
- `references/product-demo-hero.md` — When and how to build a time-driven product workflow demo in the Hero (Variant D). Includes scene design guide, 3-act structure, onEnter() callback patterns, and product-type → scene mapping table. Read this whenever the user wants to show their product's process in the hero.
