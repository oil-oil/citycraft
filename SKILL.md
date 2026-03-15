---
name: citycraft
description: Create a bold, visually striking landing page with unconventional layouts, GSAP scroll animations, SVG elements, and strong depth/layering. Use this skill whenever the user wants to build a landing page, homepage, product page, marketing page, or any single-page site that needs to impress. TRIGGER on phrases like "帮我做一个落地页", "做个首页", "landing page", "产品展示页", "官网首页", "make me a landing page", "build a homepage", "create a product page". The skill conducts a visual style interview using city imagery, generates a live style preview the user can see in their browser, then produces a complete multi-file implementation using bundled design assets.
---

# Landing Page Builder

扩展 45 城：柏林、孟买、香港、里斯本、哈瓦那、迪拜、马拉喀什、斯德哥尔摩、布宜诺斯艾利斯、墨西哥城、雷克雅未克、新加坡、圣托里尼、拉各斯、棕榈泉、伊斯坦布尔、迈阿密、成都、哥本哈根、维也纳、开普敦、波哥大、阿姆斯特丹、贝鲁特、波特兰 / 上海 / 北京 / 重庆 / 西安 / 杭州 / 深圳夜 / 敦煌 / 苏州 / 拉萨 / 罗马 / 布拉格 / 墨尔本 / 雅典 / 卡萨布兰卡 / 釜山 / 巴厘岛 / 多伦多 / 特拉维夫 / 华沙 / 孟买夜

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
| `assets/style-preview-template.html` | 50-city style preview cards | Step 2: `sed` fill `__PRODUCT_NAME__` + `__PRODUCT_HEADLINE__`, save as `style-preview.html`, open |
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

> "告诉我你的落地页是关于什么的——产品/服务名称，以及一句话介绍。另外，你大概需要哪些板块？（比如 Hero、功能介绍、案例展示、定价、FAQ、CTA 等）"

Wait for the answer before proceeding.

### Step 2: Generate the Style Preview

Use `sed` to fill in the two placeholders and open the result — do NOT read the template file into context:
- `__PRODUCT_NAME__` → the product name from Step 1
- `__PRODUCT_HEADLINE__` → a short punchy phrase (3–5 words) that captures the product's essence

```bash
_SKILL_DIR=$(ls -d ~/.agents/skills/citycraft 2>/dev/null || ls -d ~/.claude/skills/citycraft 2>/dev/null)
sed "s/__PRODUCT_NAME__/ACTUAL_PRODUCT_NAME/g; s/__PRODUCT_HEADLINE__/ACTUAL_HEADLINE/g" \
  "$_SKILL_DIR/assets/style-preview-template.html" > ./style-preview.html
open ./style-preview.html 2>/dev/null || xdg-open ./style-preview.html 2>/dev/null || echo "Open in browser: $(pwd)/style-preview.html"
```

Replace `ACTUAL_PRODUCT_NAME` and `ACTUAL_HEADLINE` with the real values from Step 1 directly in the `sed` command.

Tell the user: "我在浏览器里打开了50种城市风格的预览卡片，每个都是真实渲染效果。向下滚动可以看到全部——从京都到拉各斯到棕榈泉，再到伊斯坦布尔、迈阿密、成都、哥本哈根、维也纳、开普敦、波哥大、阿姆斯特丹、贝鲁特、波特兰，以及上海、北京、重庆、西安、杭州、深圳夜、敦煌、苏州、拉萨、罗马、布拉格、墨尔本、雅典、卡萨布兰卡、釜山、巴厘岛、多伦多、特拉维夫、华沙、孟买夜。每张卡片右上角有复制按钮，选好之后复制城市名直接告诉我。如果50个城市都不对，直接用自己的语言描述给我也行。"

### Step 3: Open the Interactive Options Preview

The user has chosen their city. Now open the visual options preview so they can *feel* the layout and nav choices instead of reading descriptions.

**3a — Look up city colors**

Read `references/city-styles.md` and find the chosen city's color tokens: `--bg`, `--surface`, `--ink`, `--muted`, `--accent`.

**3b — Generate and open options-preview.html**

Run this `sed` command, replacing the ALL-CAPS values with actual hex codes from the city. Do NOT read the template file into context:

```bash
_SKILL_DIR=$(ls -d ~/.agents/skills/citycraft 2>/dev/null || ls -d ~/.claude/skills/citycraft 2>/dev/null)
sed \
  -e "s/__PRODUCT_NAME__/ACTUAL_PRODUCT_NAME/g" \
  -e "s/__PRODUCT_HEADLINE__/ACTUAL_HEADLINE/g" \
  -e "s/__CITY_BG__/CITY_BG_VALUE/g" \
  -e "s/__CITY_SURFACE__/CITY_SURFACE_VALUE/g" \
  -e "s/__CITY_INK__/CITY_INK_VALUE/g" \
  -e "s/__CITY_MUTED__/CITY_MUTED_VALUE/g" \
  -e "s/__CITY_ACCENT__/CITY_ACCENT_VALUE/g" \
  -e "s/__CITY_DARK_BG__/#0e0c09/g" \
  -e "s/__CITY_DARK_SURFACE__/#1e1b16/g" \
  -e "s/__CITY_DARK_INK__/#f2ede4/g" \
  -e "s/__CITY_DARK_ACCENT__/CITY_ACCENT_VALUE/g" \
  -e "s/__CITY_BRIGHT_BG__/#fdf9f2/g" \
  -e "s/__CITY_BRIGHT_SURFACE__/#fffdf8/g" \
  -e "s/__CITY_BRIGHT_INK__/#1a1510/g" \
  -e "s/__CITY_BRIGHT_ACCENT__/CITY_ACCENT_VALUE/g" \
  "$_SKILL_DIR/assets/options-preview-template.html" > ./options-preview.html
open ./options-preview.html 2>/dev/null || xdg-open ./options-preview.html 2>/dev/null || echo "Open in browser: $(pwd)/options-preview.html"
```

The dark variant (`__CITY_DARK_*`) is always the luxury/night treatment — near-black bg, warm light text, same accent. The bright variant is always the fresh/modern treatment — near-white bg, dark text, same accent. The city's identity comes from the base colors and accent, not from the dark/bright shell.

Tell the user: "在浏览器里打开了一个互动选择页——有排版、导航的实际演示效果，还有三种色调的对比。可以点击全屏菜单看它怎么爆开，把光标移近底部胶囊感受磁性效果。全部选好之后，点底部的「告诉 Claude →」按钮，把结果直接粘贴给我。"

**If the user chose a non-city description** (scene, era, material, emotion): read `references/imagery-derivation.md` to derive the design token system first, use those derived colors to fill in the `sed` command above, then proceed normally.

Wait for the user to come back with their 3 choices (layout + nav + color tone) before proceeding to Step 4.

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

#### Section Assembly

**All section templates are designed to combine freely.** Each section uses CSS custom properties (`var(--bg)`, `var(--accent)`, etc.) that all resolve to the same city design tokens — so any combination stays visually coherent. There is no fixed page structure: build the order that fits the product's story. Common sequences:

- Landing for a SaaS tool: Hero D → Features C (timeline) → Features A (big numbers) → Pricing → FAQ A → CTA
- Agency portfolio: Hero A → Features B (alternating) → Testimonials → CTA
- Developer tool: Hero B → Features C → Features A → Pricing → FAQ B → CTA
- Luxury product: Hero C → Features B → Testimonials → CTA

Before writing code, plan which section templates to use from the bundled assets:

| If the user needs... | Use this template | From file |
|---------------------|-------------------|-----------|
| Hero — massive bold statement | Variant A (全屏铺张) | `assets/sections/hero-variants.html` |
| Hero — product visual + headline | Variant B (分屏张力) | `assets/sections/hero-variants.html` |
| Hero — elegant, story-first | Variant C (极简下降) | `assets/sections/hero-variants.html` |
| Hero — product has a workflow to show | Variant D (产品演示型) | `assets/sections/hero-variants.html` + `references/product-demo-hero.md` |
| Hero — typography-led, high-impact statement | Variant E (文字爆炸型) | `assets/sections/hero-variants.html` |
| Hero — editorial storytelling with asymmetry | Variant F (杂志撕裂型) | `assets/sections/hero-variants.html` |
| Hero — playful product launch / card spotlight | Variant G (弹出卡片型) | `assets/sections/hero-variants.html` |
| Features — data/metrics focus | Variant A (大数字) | `assets/sections/features-variants.html` |
| Features — product screenshots/visuals | Variant B (交替展示) | `assets/sections/features-variants.html` |
| How it works — step-by-step | Variant C (时间线) | `assets/sections/features-variants.html` |
| Features — modular story blocks / mixed emphasis | Variant D (本托格子型) | `assets/sections/features-variants.html` |
| Features — browseable capability ribbon | Variant E (水平滚动卡带型) | `assets/sections/features-variants.html` |
| Features — objection handling / expandable detail | Variant F (问答展开型) | `assets/sections/features-variants.html` |
| Pricing | 定价表 | `assets/sections/conversion-variants.html` |
| Pricing — plan comparison with monthly/yearly toggle | 对比定价表 | `assets/sections/conversion-variants.html` |
| Social proof / testimonials | 引言墙 | `assets/sections/conversion-variants.html` |
| Social proof / trusted customers | 品牌墙 | `assets/sections/conversion-variants.html` |
| Final CTA | 强力CTA区 | `assets/sections/conversion-variants.html` |
| FAQ — editorial, large "FAQ" anchor left | Variant A (编辑排版型) | `assets/sections/conversion-variants.html` |
| FAQ — card grid, 2 columns, expands in place | Variant B (全宽焦点型) | `assets/sections/conversion-variants.html` |

Read the relevant section files, copy the `<section>` + `<style>` blocks, then adapt the copy and apply the city's design tokens.

#### index.html
- Load GSAP + ScrollTrigger CDN:
  ```html
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
  ```
- Link `style.css` and `main.js`
- Write real product copy — not Lorem Ipsum. The copy should fit the chosen city aesthetic's tone of voice.

#### style.css
- At `:root`: full design token system (colors, fonts, spacing, radii) from the chosen city style in `references/city-styles.md`
- **Texture**: for cities 1–5 (京都/巴黎/东京夜/纽约/首尔), copy the matching class from `assets/textures.css`. For cities 6–50, copy the texture CSS directly from the `### Texture` section in `references/city-styles.md`
- **Copy** at least 2 clip-path classes from `assets/clip-paths.css` and apply them to sections
- `clamp()` for ALL headline font sizes — use these reference ranges (going bigger defeats the design, the whitespace and composition carry the impact):
  - Hero 主标题：`clamp(2.8rem, 7vw, 7rem)` — 铺张型也不超过 7rem
  - Section 标题：`clamp(2rem, 4vw, 4rem)`
  - 大数字/装饰数字：`clamp(4rem, 10vw, 9rem)`
  - 副标题/说明文字：`clamp(1rem, 1.4vw, 1.2rem)`
- The nav CSS matching the selected nav style (see `references/nav-catalog.md`)

#### main.js
- Register ScrollTrigger: `gsap.registerPlugin(ScrollTrigger)`
- **Copy** the relevant animation functions from `assets/gsap-snippets.js` and call them. Required minimum:
  1. `initHeroEntrance()` — stagger hero elements in
  2. `initParallax()` — at least 2 layers at different speeds
  3. Section reveals — each heading animates in on viewport entry
  4. `initStickySteps()` OR `initBlastMenu()` OR `initMagneticPill()` — whichever matches the nav/layout
- All functions should call `ScrollTrigger.refresh()` after fonts load

#### assets/icons.svg
- SVG sprite with `<symbol>` elements
- At minimum: logo mark, nav toggle (open/close), arrow, checkmark, 2–3 product-relevant feature icons
- Icon style must match the city aesthetic: stroke weight, corner style, visual weight (see `references/city-styles.md` icon descriptions)

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
- `references/imagery-derivation.md` — How to translate any non-city description (scene, era, material, emotion) into a concrete design token system. Read this whenever the user describes something that isn't one of the 50 city cards.
- `references/product-demo-hero.md` — When and how to build a time-driven product workflow demo in the Hero (Variant D). Includes scene design guide, 3-act structure, onEnter() callback patterns, and product-type → scene mapping table. Read this whenever the user wants to show their product's process in the hero.
