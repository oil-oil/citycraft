---
name: citycraft
description: "使用城市风格库与可选交互预览，为产品、活动、营销或品牌创建具有鲜明风格的完整落地页，输出 HTML、CSS、JS 和 SVG。用户要求有视觉表现力的单页网站或明确使用 citycraft 时使用。不用于普通后台、组件修复、静态海报或不允许改变品牌设计的局部维护；已有产品信息和用户选定风格时直接复用。"
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
| `assets/options-preview-template.html` | Interactive demos: nav styles, color variants, transition styles, hero/features/testimonials variants | Step 3: `sed` fill city color tokens + product name, save as `options-preview.html`, open |
| `assets/textures.css` | 6 CSS texture classes (`.texture-kyoto`, `.texture-paris`, `.texture-tokyo`, etc.) | Copy the matching class into `style.css` |
| `assets/gsap-snippets.js` | 6 GSAP animation functions (blur entrance, line reveal, parallax, sticky steps, blast menu, magnetic pill) | Copy the relevant functions into `main.js` |
| `assets/clip-paths.css` | 8 clip-path divider classes (`.clip-diagonal-br`, `.clip-parallelogram`, `.clip-arc-bottom`, etc.) | Use at least 2 in `style.css` for section dividers |
| `assets/sections/hero-variants.html` | 3 Hero section templates (全屏铺张/分屏张力/极简下降) | Step 4: pick the variant matching the user's typography preference, copy and adapt |
| `assets/sections/features-variants.html` | 6 Features section templates (大数字/交替展示/时间线/本托格子/水平滚动/问答展开) | Step 4: pick based on content type (stats → big number, how-it-works → timeline) |
| `assets/sections/testimonial-variants.html` | 6 Testimonials templates (紧凑卡片/单列引用/马赛克拼贴/滚动横条/对话气泡/头像墙) | Step 4: pick based on testimonial volume and visual style preference |
| `assets/sections/conversion-variants.html` | Pricing table, FAQ, brand wall, power CTA | Step 4: copy relevant section, all use CSS custom properties |
| `references/product-demo-hero.md` | Product demo hero principles + scene design guide | Read when user wants to show product workflow in hero (see Step 3/4) |

**The quality guarantee of this skill comes from using these assets.** They encode specific design decisions that make outputs distinct. Don't describe what to do — copy the code and adapt it.

---

## The Workflow

### Step 1: Understand the Product

复用用户已经给出的产品与风格；只在产品信息缺失时询问：

> "告诉我你的落地页是关于什么的——产品/服务名称，以及一句话介绍。"

用户已给出产品说明、已选择城市或已委托 Agent 决策时，直接进入相应步骤。

### Step 2–3：可选风格与布局预览

用户已有选择时直接复用；让 Agent 选择时读取相关城市条目，说明理由后继续。需要比较时按 [预览工作流](references/preview-workflow.md) 生成本地预览。没有可用预览能力时在对话中提供少量候选，不把打开页面当成用户已经选定。

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
_SKILL_DIR="<当前 Skill 的绝对目录>"
_OUT="./{product-name}-landing"
mkdir -p "$_OUT/assets"
```

**Step 2 — Assemble section variants into a staging file**

Plan which variants to use (see table below), then pipe each into a staging file:

```bash
# Replace B / C / B / PRICING with the user's actual choices
python3 "$_SKILL_DIR/assets/scripts/extract_variant.py" \
  "$_SKILL_DIR/assets/sections/hero-variants.html" B > "$_OUT/_sections.html"
python3 "$_SKILL_DIR/assets/scripts/extract_variant.py" \
  "$_SKILL_DIR/assets/sections/features-variants.html" C >> "$_OUT/_sections.html"
python3 "$_SKILL_DIR/assets/scripts/extract_variant.py" \
  "$_SKILL_DIR/assets/sections/testimonial-variants.html" B >> "$_OUT/_sections.html"
python3 "$_SKILL_DIR/assets/scripts/extract_variant.py" \
  "$_SKILL_DIR/assets/sections/conversion-variants.html" PRICING >> "$_OUT/_sections.html"
python3 "$_SKILL_DIR/assets/scripts/extract_variant.py" \
  "$_SKILL_DIR/assets/sections/conversion-variants.html" CTA >> "$_OUT/_sections.html"
```

For testimonials use: `A`, `B`, `C`, `D`, `E`, `F`
For conversion sections use: `PRICING`, `COMPARE_PRICING`, `BRAND_WALL`, `CTA`, `FAQ_A`, `FAQ_B`

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
- SaaS tool: Hero D → Features C → Features A → Testimonials A → Pricing → FAQ A → CTA
- Agency portfolio: Hero A → Features B → Testimonials C → CTA
- Developer tool: Hero B → Features C → Features A → Testimonials A → Pricing → FAQ B → CTA
- Luxury product: Hero C → Features B → Testimonials B → CTA
- B2C app: Hero E → Features E → Testimonials F → CTA

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
| Testimonials — compact grid | 紧凑卡片网格 | A |
| Testimonials — magazine style | 单列引用墙 | B |
| Testimonials — masonry layout | 马赛克拼贴 | C |
| Testimonials — horizontal scroll | 滚动横条 | D |
| Testimonials — conversation bubbles | 对话气泡 | E |
| Testimonials — avatar wall | 视频头像墙 | F |
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
- Break template uniformity: vary visual weight across items within each section. The template shows a repeating pattern — make one item the focal point (accent background, larger card, featured badge, different internal layout) and let others recede. No section should look like a grid of clones.

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
3. **Decide the transition type independently for each section boundary.** Every pair of adjacent sections has its own visual relationship — don't reuse the same clip-path class everywhere. The user chooses a **transition direction** (geometric sharp / organic soft / cover-blend / minimal line / AI auto) in the options preview. Use that direction to constrain which classes you pick: `GEOMETRIC` → diagonals, chamfers, steps; `ORGANIC` → curves, scallops, arcs; `BLEND` → cover overlays and gradient dissolves; `MINIMAL` → hairline rules. If `__AI_CHOOSE__`, scan the selected city's entry in `references/city-styles.md` for divider/transition language first. Then apply per-boundary logic: consider what the two sections are (hero → features, features → pricing, etc.), their relative energy, and the overall page rhythm. Available classes in `assets/clip-paths.css`: diagonal (`clip-diagonal-*`, `clip-parallelogram`), curved (`clip-round-bottom`, `clip-scallop`, `clip-arc-bottom`), gradient dissolve (`section-dissolve`), flat rule (`section-rule`).
4. **No generic icons.** Match the city style's stroke weight and geometry.
5. **Two typefaces minimum.** Display/serif for headlines + clean sans for body. From `references/city-styles.md`. Decorative/script accent fonts (when a city style mentions one) go on watermarks, pull quotes, or ornamental elements — **never on buttons, nav, or body copy**.
6. **Nav must surprise.** Use the chosen nav from `references/nav-catalog.md` with its full surprise element implemented.
7. **Use bundled assets.** The texture, GSAP snippets, and clip-paths must come from the skill's asset files — not reimplemented from scratch.
8. **`.line-wrap` CJK fix.** Whenever the page has Chinese or Japanese text and uses `.line-wrap { overflow: hidden }` for line reveal animations, add `padding-top: 0.15em; margin-top: -0.15em;` to prevent CJK ascenders from being clipped at the top.
9. **No clone grids.** When a section contains multiple repeating items (feature rows, pricing cards, FAQ items, testimonials), they must not all share the same visual treatment. One item should be the focal point — larger, accented, or with a distinct layout — while others form the supporting cast. A section should feel like a poster with visual hierarchy, not a spreadsheet of identical rows. This is the single biggest cause of pages looking "templated" rather than designed.

---

## Reference Files

- `references/city-styles.md` — Exact design parameters (fonts, colors, textures, motion, icons) for each city aesthetic
- `references/nav-catalog.md` — 4 nav styles with full implementation notes and GSAP code
- `references/imagery-derivation.md` — How to translate any non-city description (scene, era, material, emotion) into a concrete design token system. Read this whenever the user describes something that isn't one of the 57 city cards.
- `references/product-demo-hero.md` — When and how to build a time-driven product workflow demo in the Hero (Variant D). Includes scene design guide, 3-act structure, onEnter() callback patterns, and product-type → scene mapping table. Read this whenever the user wants to show their product's process in the hero.

## 事实与降级

模板里的评价、客户 Logo、人数与价格仅为结构示例；没有证据就删除或换成真实产品说明，不编造背书。实现需支持键盘操作、`prefers-reduced-motion` 和脚本/CDN 加载失败时的静态可读内容。视觉验收说明实际检查的视口与状态；未渲染时不能声称视觉已通过。
