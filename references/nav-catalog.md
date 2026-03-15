# Nav Style Catalog

Four navigation archetypes. Each has a distinct personality and technical approach.

---

## Nav A: 全屏爆开式 (Full-screen Blast)

**适合**: 东京夜、纽约 — high-drama brands, agencies, portfolios

**视觉效果**: The hamburger icon triggers a full-screen overlay that **covers the entire viewport**. Menu items stagger in one by one at large type sizes. The background of the overlay often has a visual motif (noise, gradient, or the site's accent color flooding in).

**Surprise element**: The "close" animation runs in reverse — the full screen shrinks back into the hamburger button.

**Implementation notes**:
```js
// GSAP timeline for open
const tl = gsap.timeline();
tl.to(".nav-overlay", { clipPath: "inset(0% 0% 0% 0%)", duration: 0.6, ease: "power4.inOut" })
  .from(".nav-item", { y: 60, opacity: 0, stagger: 0.08, duration: 0.5, ease: "power3.out" }, "-=0.2");

// Overlay starts as clipPath: "inset(0% 0% 100% 0%)" (hidden from bottom)
```

**Desktop behavior**: On wider screens, show links inline in the header. The full-screen menu is mobile-focused, but can also be triggered on desktop for dramatic effect.

---

## Nav B: 底部磁性胶囊 (Bottom Magnetic Pill)

**适合**: 首尔、巴黎 — modern, friendly, unconventional placement

**视觉效果**: Navigation is a **small floating pill fixed to the bottom center** of the viewport (not the top). Links are compact and tight. On hover, links subtly expand or shift.

**Surprise element**: The pill is "magnetic" — it has a slight attraction to the cursor when the cursor is within ~80px of it. Implemented with GSAP `mousemove` listener.

**Implementation notes**:
```js
const pill = document.querySelector(".pill-nav");
document.addEventListener("mousemove", (e) => {
  const rect = pill.getBoundingClientRect();
  const pillCx = rect.left + rect.width / 2;
  const pillCy = rect.top + rect.height / 2;
  const dx = e.clientX - pillCx;
  const dy = e.clientY - pillCy;
  const dist = Math.sqrt(dx * dx + dy * dy);
  const maxDist = 120;
  if (dist < maxDist) {
    const pull = 1 - dist / maxDist;
    gsap.to(pill, { x: dx * pull * 0.25, y: dy * pull * 0.25, duration: 0.4, ease: "power2.out" });
  } else {
    gsap.to(pill, { x: 0, y: 0, duration: 0.6, ease: "elastic.out(1, 0.5)" });
  }
});
```

**CSS**:
```css
.pill-nav {
  position: fixed;
  bottom: 28px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 100;
  background: rgba(255,255,255,0.12);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(255,255,255,0.15);
  border-radius: 100px;
  padding: 10px 24px;
  display: flex;
  gap: 28px;
  align-items: center;
}
```

---

## Nav C: 侧边垂直型 (Vertical Side Rail)

**适合**: 京都、巴黎 — editorial, portfolio, photography

**视觉效果**: Navigation runs **vertically along the left edge** of the viewport, fixed. Links are rotated 90° and read bottom-to-top. The logo sits at the top of the rail. The active section is highlighted.

**Surprise element**: As you scroll, a thin progress line draws down the rail. Each nav item "fills in" as its section is reached.

**Implementation notes**:
```css
.side-nav {
  position: fixed;
  left: 24px;
  top: 50%;
  transform: translateY(-50%);
  z-index: 100;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 32px;
}

.side-nav a {
  writing-mode: vertical-lr;  /* vertical-lr reads top→bottom for both Latin and CJK */
                               /* do NOT use vertical-rl + rotate(180deg) — flips CJK characters */
                               /* active/hover state: only change color/opacity, NO rotate transform */
  font-size: 0.7rem;
  letter-spacing: 0.15em;
  text-transform: uppercase;
}
```

**ScrollTrigger integration**:
```js
sections.forEach((section, i) => {
  ScrollTrigger.create({
    trigger: section,
    start: "top center",
    end: "bottom center",
    onEnter: () => setActiveNavItem(i),
    onEnterBack: () => setActiveNavItem(i),
  });
});
```

---

## Nav D: 拆分居中型 (Split Centered)

**适合**: 任何风格 — clean, structured, editorial

**视觉效果**: Logo floats at absolute center. Nav links split into **left group** and **right group** flanking the logo. The CTA button appears on the far right. This creates perfect visual balance.

**Surprise element**: On scroll past ~100px, the nav compresses: the center logo shrinks and the layout shifts to a traditional left-logo arrangement — animated smoothly with GSAP.

**Implementation notes**:
```html
<nav class="split-nav">
  <div class="nav-left">
    <a href="#features">Features</a>
    <a href="#how">How it works</a>
  </div>
  <a href="/" class="nav-logo">Brand</a>
  <div class="nav-right">
    <a href="#pricing">Pricing</a>
    <a href="#faq">FAQ</a>
    <a href="#start" class="nav-cta">Get Started</a>
  </div>
</nav>
```

```js
ScrollTrigger.create({
  start: "top top",
  end: "+=100",
  onUpdate: (self) => {
    if (self.progress > 0.5 && !isCompressed) {
      gsap.to(".split-nav", { /* compress layout */ });
      isCompressed = true;
    } else if (self.progress <= 0.5 && isCompressed) {
      gsap.to(".split-nav", { /* expand layout */ });
      isCompressed = false;
    }
  }
});
```
