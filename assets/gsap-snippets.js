/* ============================================================
   LANDING PAGE SKILL — GSAP ANIMATION SNIPPETS
   These are proven patterns. Copy, adapt variable names,
   and plug into your main.js. Do NOT reinvent these.
   ============================================================ */

// ─── 1. BLUR-STAGGER ENTRANCE (hero text reveal) ──────────────
// Usage: call once on DOMContentLoaded
function initHeroEntrance(containerSelector, itemSelector) {
  gsap.from(itemSelector || `${containerSelector} > *`, {
    y: 32,
    opacity: 0,
    filter: "blur(6px)",
    duration: 0.9,
    ease: "power3.out",
    stagger: 0.12,
    clearProps: "filter",
  });
}
// Example: initHeroEntrance(".hero-text", ".hero-text > *")


// ─── 2. CLIP-MASK LINE REVEAL (Paris / editorial style) ────────
// Each heading line slides up from a clip container.
// Wrap each line: <span class="line-wrap"><span class="line-inner">text</span></span>
//
// ⚠️  CJK CLIPPING FIX (required when page includes Chinese/Japanese):
// .line-wrap { overflow: hidden } clips tall CJK ascenders at the top.
// Always add this compensation in style.css:
//   .line-wrap { overflow: hidden; padding-top: 0.15em; margin-top: -0.15em; }
function initLineReveal(headingSelector) {
  const headings = document.querySelectorAll(headingSelector);
  headings.forEach((heading) => {
    const lines = heading.querySelectorAll(".line-inner");
    gsap.from(lines, {
      y: "110%",
      duration: 0.85,
      ease: "expo.out",
      stagger: 0.08,
      scrollTrigger: {
        trigger: heading,
        start: "top 80%",
        toggleActions: "play none none none",
      },
    });
  });
}
// CSS required:
// .line-wrap { display: block; overflow: hidden; }
// .line-inner { display: block; }


// ─── 3. PARALLAX LAYERS (depth on scroll) ──────────────────────
// Pass an array of { selector, speed } — speed 0.5 = half rate, 1.5 = faster
function initParallax(layers) {
  layers.forEach(({ selector, speed }) => {
    gsap.to(selector, {
      y: () => window.innerHeight * (speed - 1) * -0.4,
      ease: "none",
      scrollTrigger: {
        trigger: "body",
        start: "top top",
        end: "bottom bottom",
        scrub: speed,
      },
    });
  });
}
// Example:
// initParallax([
//   { selector: ".hero-bg-glow",   speed: 0.6 },
//   { selector: ".hero-phone",     speed: 1.2 },
//   { selector: ".hero-particles", speed: 0.8 },
// ]);


// ─── 4. STICKY STEP-THROUGH (how it works / theatrical) ────────
// Pins a container, steps through items as user scrolls.
// HTML: <div class="steps-wrapper">
//         <div class="steps-panel sticky-panel">  ← pinned
//         <div class="steps-content">             ← scroll height
//           <div class="step" data-step="0">
function initStickySteps(wrapperSelector, panelSelector, stepSelector) {
  const steps = document.querySelectorAll(stepSelector);
  const total = steps.length;

  ScrollTrigger.create({
    trigger: wrapperSelector,
    start: "top top",
    end: `+=${total * 100}vh`,
    pin: panelSelector,
    scrub: false,
    onUpdate(self) {
      const idx = Math.min(Math.floor(self.progress * total), total - 1);
      steps.forEach((s, i) => s.classList.toggle("active", i === idx));
    },
  });
}
// Example:
// initStickySteps(".how-wrapper", ".how-panel", ".how-step")


// ─── 5. FULLSCREEN BLAST MENU ──────────────────────────────────
// Open/close animation for a full-viewport nav overlay.
// HTML: <div class="nav-overlay"> <a class="nav-item">...</a> </div>
function initBlastMenu(triggerSelector, overlaySelector, itemSelector) {
  const trigger = document.querySelector(triggerSelector);
  const overlay = document.querySelector(overlaySelector);
  const items   = document.querySelectorAll(itemSelector);
  let isOpen = false;

  // Overlay starts: clip-path: inset(0% 0% 100% 0%)
  gsap.set(overlay, { clipPath: "inset(0% 0% 100% 0%)", display: "flex" });

  const openTl = gsap.timeline({ paused: true })
    .to(overlay,  { clipPath: "inset(0% 0% 0% 0%)", duration: 0.6, ease: "power4.inOut" })
    .from(items,  { y: 64, opacity: 0, stagger: 0.07, duration: 0.5, ease: "power3.out" }, "-=0.25");

  trigger.addEventListener("click", () => {
    isOpen = !isOpen;
    trigger.setAttribute("aria-expanded", isOpen);
    document.body.style.overflow = isOpen ? "hidden" : "";
    isOpen ? openTl.play() : openTl.reverse();
  });

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && isOpen) { isOpen = false; openTl.reverse(); document.body.style.overflow = ""; }
  });
}
// CSS required:
// .nav-overlay { position: fixed; inset: 0; z-index: 200; display: none; }
// Call: initBlastMenu(".menu-toggle", ".nav-overlay", ".nav-item")


// ─── 6. MAGNETIC PILL NAV ──────────────────────────────────────
// Bottom pill floats toward the cursor when nearby.
function initMagneticPill(pillSelector, radius, strength) {
  radius   = radius   || 120;
  strength = strength || 0.28;
  const pill = document.querySelector(pillSelector);
  if (!pill) return;

  document.addEventListener("mousemove", (e) => {
    const r    = pill.getBoundingClientRect();
    const cx   = r.left + r.width  / 2;
    const cy   = r.top  + r.height / 2;
    const dx   = e.clientX - cx;
    const dy   = e.clientY - cy;
    const dist = Math.hypot(dx, dy);

    if (dist < radius) {
      const pull = 1 - dist / radius;
      gsap.to(pill, { x: dx * pull * strength, y: dy * pull * strength, duration: 0.4, ease: "power2.out" });
    } else {
      gsap.to(pill, { x: 0, y: 0, duration: 0.8, ease: "elastic.out(1, 0.5)" });
    }
  });
}
// Example: initMagneticPill(".pill-nav")


// ─── 7. HERO DEMO STEPPER (time-driven product walkthrough) ────
// A self-running, scene-by-scene product demo inside the Hero.
// NOT scroll-driven — advances on a timer, resets when scrolled away.
//
// Required HTML structure:
//   <div class="demo-wrapper">                    ← IntersectionObserver target
//     <div class="demo-step-badge">
//       <span class="demo-step-num"></span>
//       <span class="demo-step-label"></span>
//     </div>
//     <div class="demo-panel">                    ← needs overflow: visible in CSS
//       <div class="demo-slot" data-step="0"></div>
//       <div class="demo-slot" data-step="1"></div>
//       <div class="demo-slot" data-step="2"></div>
//     </div>
//     <div class="demo-progress-dots">
//       <span class="step-dot active" data-target="0"></span>
//       <span class="step-dot" data-target="1"></span>
//       <span class="step-dot" data-target="2"></span>
//     </div>
//     <!-- Optional synced subtitle — text updates per step -->
//     <p class="demo-synced-text"
//        data-step-0="Step 0 subtitle"
//        data-step-1="Step 1 subtitle"
//        data-step-2="Step 2 subtitle"></p>
//   </div>
//
// stepDefs: array of { num, label, onEnter(slotEl) }
// onEnter receives the slot DOM element — run your GSAP timeline inside it.
//
// Design law: each onEnter should animate (1) one hero element first,
// (2) supporting elements with stagger delay, (3) one breakout element last.
// Read references/product-demo-hero.md before writing these callbacks.
function initHeroDemoStepper(wrapperSel, stepDefs, intervalMs) {
  const wrapper = document.querySelector(wrapperSel);
  if (!wrapper) return;
  intervalMs = intervalMs || 3200;

  const slots    = wrapper.querySelectorAll('.demo-slot');
  const numEl    = wrapper.querySelector('.demo-step-num');
  const labelEl  = wrapper.querySelector('.demo-step-label');
  const dots     = wrapper.querySelectorAll('.step-dot');
  const syncText = wrapper.querySelector('.demo-synced-text');

  let current = -1;
  let timer   = null;

  function updateBadge(idx) {
    const def = stepDefs[idx];
    if (numEl) {
      gsap.to(numEl, { opacity: 0, y: -6, duration: 0.18, onComplete: () => {
        numEl.textContent = def.num;
        gsap.to(numEl, { opacity: 1, y: 0, duration: 0.22 });
      }});
    }
    if (labelEl) {
      gsap.to(labelEl, { opacity: 0, duration: 0.15, onComplete: () => {
        labelEl.textContent = def.label;
        gsap.to(labelEl, { opacity: 1, duration: 0.2 });
      }});
    }
    if (syncText) {
      gsap.to(syncText, { opacity: 0, y: 4, duration: 0.18, onComplete: () => {
        syncText.textContent = syncText.dataset['step' + idx] || '';
        gsap.to(syncText, { opacity: 1, y: 0, duration: 0.25 });
      }});
    }
    dots.forEach((d, i) => d.classList.toggle('active', i === idx));
  }

  function enterSlot(slot, idx) {
    gsap.set(slot, { display: 'block', opacity: 0 });
    gsap.to(slot, { opacity: 1, duration: 0.22 });
    if (stepDefs[idx].onEnter) stepDefs[idx].onEnter(slot);
  }

  function goTo(idx) {
    const prev = current;
    current = idx;
    updateBadge(idx);
    if (prev >= 0 && slots[prev]) {
      gsap.to(slots[prev], { opacity: 0, duration: 0.2, onComplete: () => {
        gsap.set(slots[prev], { display: 'none' });
        enterSlot(slots[idx], idx);
      }});
    } else {
      enterSlot(slots[idx], idx);
    }
  }

  function startTimer() {
    clearInterval(timer);
    timer = setInterval(() => goTo((current + 1) % stepDefs.length), intervalMs);
  }

  dots.forEach((dot, i) => {
    dot.addEventListener('click', () => { clearInterval(timer); goTo(i); startTimer(); });
  });

  // Start on viewport entry, pause on exit, reset when re-entering
  const io = new IntersectionObserver((entries) => {
    entries.forEach(({ isIntersecting }) => {
      if (isIntersecting) {
        slots.forEach(s => gsap.set(s, { display: 'none', opacity: 0 }));
        current = -1;
        goTo(0);
        startTimer();
      } else {
        clearInterval(timer);
      }
    });
  }, { threshold: 0.3 });

  io.observe(wrapper);
}
// Example:
// initHeroDemoStepper(".demo-wrapper", [
//   { num: "01", label: "Setup",   onEnter(slot) { /* gsap animations */ } },
//   { num: "02", label: "Running", onEnter(slot) { animateCount(slot.querySelector('.big-num'), 4200, 1.5); } },
//   { num: "03", label: "Result",  onEnter(slot) { /* gsap animations */ } },
// ]);


// ─── 8. ANIMATED COUNT (use inside initHeroDemoStepper onEnter) ─
// Counts from 0 → target inside an element. Shows velocity and scale.
function animateCount(el, target, duration, suffix) {
  if (!el) return;
  suffix   = suffix   || '';
  duration = duration || 1.6;
  const obj = { val: 0 };
  gsap.to(obj, {
    val: target,
    duration: duration,
    ease: 'power3.out',
    onUpdate: () => { el.textContent = Math.round(obj.val).toLocaleString() + suffix; },
  });
}
// Example: animateCount(slot.querySelector('.views-num'), 84201, 1.8)
// Example: animateCount(slot.querySelector('.pct'), 96, 1.2, '%')
