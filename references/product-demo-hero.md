# Product Demo Hero — Design Principles

Use Hero Variant D (产品演示型) when the product has a **process** — a workflow, a pipeline, a transformation — that users need to understand before they commit. The right side of the hero becomes a self-running film of that process.

**Trigger signals from the user:**
- "展示我们产品的工作流程"
- "我想让用户一看就明白怎么用"
- "右边放一个演示"
- "有几个步骤想展示出来"
- Any SaaS, dev tool, AI product, or platform with 3–5 distinct operational phases

---

## The 6 Universal Principles

### 1. 时间驱动，非滚动驱动
Scenes advance on a timer (~3 seconds each), not on scroll. The visitor does nothing — the product introduces itself. Use `setInterval` + `IntersectionObserver` (reset when scrolled away, restart when back in view). See `initHeroDemoStepper()` in `assets/gsap-snippets.js`.

### 2. 每帧 = 一个英雄 + 一群配角
Every scene has one **focal element** — the thing the eye goes to first. It enters immediately: `opacity 0→1, scale 0.92→1`. Supporting elements (labels, badges, sub-stats) enter after it, staggered. Never animate 5 things at the same speed — it reads as noise.

### 3. overflow: visible 让元素破框
The demo panel is not a cage. Cards, badges, numbers, small phone mockups can spill **outside** the panel boundary — positioned with negative coordinates. This creates spatial depth and makes the demo feel alive rather than trapped in a box.

### 4. 步骤指示器是"场外旁白"
The step number + label floats **outside** the top-left corner of the panel (e.g., `top: -24px; left: -32px`). It doesn't compete with the scene content. It tells the visitor "we're on scene 2 of 4" without cluttering the stage.

### 5. 每个场景讲一件正在发生的事
Don't show a static screenshot. Simulate a **moment in progress**:
- Not "here is the dashboard" → "analysis running: 96% complete"
- Not "see our users" → "deploying 20 creators, connections forming"
- Not "results view" → numbers counting up from zero, chart drawing itself

Present-tense, active, alive.

### 6. 数字动画传达规模感
When a scene has a metric (users, views, records processed), animate it **from 0 to target** within the scene. This is not decoration — the counting motion communicates velocity and scale in a way static numbers never can. Use `animateCount()` from `assets/gsap-snippets.js`.

---

## Scene Design Guide

### How many scenes?
3 is the minimum. 4 is ideal. 5 is the maximum before it feels like a tutorial. Each scene should correspond to a **phase** the user recognizes from their own work.

### The universal 3-act structure
Almost every product maps onto:

| Act | What it shows | Design focus |
|-----|--------------|--------------|
| **01 · Input / Setup** | User tells the product what they want | Form rows appearing, fields populating, tags floating in |
| **02 · Process / Run** | Product does its work | Network connecting, progress bars, nodes activating, scan lines |
| **03 · Output / Result** | What the user gets | Big number counting up, chart drawing, success badge |

For 4-scene products, split Act 2 into two phases: "dispatching" and "running."

### Per-scene anatomy

Each scene needs exactly three things:

1. **Hero element** — enters first, commands attention. Can be: a card, a large number, a phone mockup, an SVG diagram. Keep it to one.

2. **Supporting elements** (2–4) — float around the hero. Can be: tag pills, stat badges, status capsules, small charts. Each enters with a delay of +0.15–0.3s after the hero.

3. **Breakout element** — one element that deliberately crosses the panel boundary. This is what gives the scene dimensionality. Can be: a badge with `bottom: -20px`, a card with `right: -24px`, a label with `top: -16px`.

---

## Product Type → Scene Ideas

| Product | Scene 01 | Scene 02 | Scene 03 |
|---------|----------|----------|----------|
| AI content tool | Paste URL / input | AI analyzing / generating | Output card with content pieces |
| Developer database | Schema definition | Query executing | Results table + latency stat |
| Email / outreach | Audience config | Sending in progress | Open rate + reply count |
| Analytics platform | Connect data source | Processing rows | Dashboard with chart |
| HR / recruiting | Job description input | Candidate matching | Top matches with scores |
| Finance / billing | Invoice data | Categorizing / reconciling | Summary + savings number |
| Design tool | Upload assets | AI composing | Generated variants grid |

---

## Writing onEnter() Callbacks

Each scene's animation runs inside the `onEnter(slotEl)` callback passed to `initHeroDemoStepper()`. Think of it as a director calling "action" on that scene.

```javascript
{
  num: "01",
  label: "Analyzing",
  onEnter(slot) {
    // Hero element enters first
    gsap.fromTo(slot.querySelector('.scene-card'),
      { opacity: 0, y: 28, scale: 0.94 },
      { opacity: 1, y: 0, scale: 1, duration: 0.55, ease: "power3.out" }
    );
    // Supporting elements stagger in after
    gsap.fromTo(slot.querySelectorAll('.scene-tag'),
      { opacity: 0, scale: 0.8, y: 8 },
      { opacity: 1, scale: 1, y: 0, duration: 0.4, stagger: 0.12, delay: 0.3, ease: "back.out(1.4)" }
    );
    // Breakout badge slides from left
    gsap.fromTo(slot.querySelector('.scene-breakout'),
      { opacity: 0, x: -16 },
      { opacity: 1, x: 0, duration: 0.4, delay: 0.55, ease: "power3.out" }
    );
    // If scene has a counter — animate it
    animateCount(slot.querySelector('.scene-count'), 84201, 1.8);
  }
}
```

---

## The Left-Side Text Syncs With Steps

Don't keep the hero headline static while the right side changes scenes. Use `.demo-synced-text` (a `<p>` with `data-step-0`, `data-step-1`, `data-step-2` attributes) to make the subtitle update with each scene. One line of context per step — not a full sentence, just a crisp phrase that reinforces what the user is seeing.

Example:
```html
<p class="demo-synced-text"
   data-step-0="Tell us your audience and goal"
   data-step-1="AI matches 40 creator profiles"
   data-step-2="Views verified, billing starts">
</p>
```

`initHeroDemoStepper()` handles the fade-transition automatically.
