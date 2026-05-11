/* ==========================================================================
   Hoffman Legal — Modern Polish Pass
   Shared behavior for sticky CTA, back-to-top, progress bar, scroll reveal
   Zero dependencies. Safe to load on every page.
   ========================================================================== */
(function () {
  'use strict';

  var doc = document;
  var root = doc.documentElement;
  var body = doc.body;

  // --------------------------------------------------------------------------
  // Reading progress bar
  // --------------------------------------------------------------------------
  function initProgressBar() {
    var bar = doc.querySelector('.read-progress');
    if (!bar) return;

    var ticking = false;
    function update() {
      var scrollTop = window.pageYOffset || root.scrollTop;
      var height = root.scrollHeight - root.clientHeight;
      var pct = height > 0 ? Math.min(100, (scrollTop / height) * 100) : 0;
      bar.style.width = pct + '%';
      ticking = false;
    }
    function onScroll() {
      if (!ticking) {
        window.requestAnimationFrame(update);
        ticking = true;
      }
    }
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll);
    update();
  }

  // --------------------------------------------------------------------------
  // Back-to-top button
  // --------------------------------------------------------------------------
  function initBackToTop() {
    var btn = doc.querySelector('.back-to-top');
    if (!btn) return;

    function toggle() {
      if ((window.pageYOffset || root.scrollTop) > 600) {
        btn.classList.add('is-visible');
      } else {
        btn.classList.remove('is-visible');
      }
    }
    window.addEventListener('scroll', toggle, { passive: true });
    btn.addEventListener('click', function () {
      try {
        window.scrollTo({ top: 0, behavior: 'smooth' });
      } catch (e) {
        window.scrollTo(0, 0);
      }
    });
    toggle();
  }

  // --------------------------------------------------------------------------
  // Sticky mobile CTA bar
  //   Hidden until the user scrolls past the hero (or 400px on inner pages).
  // --------------------------------------------------------------------------
  function initMobileCtaBar() {
    var bar = doc.querySelector('.mobile-cta-bar');
    if (!bar) return;

    body.classList.add('has-mobile-cta');

    // Trigger sits a bit below hero on the homepage, or 400px in on inner pages.
    var triggerY = 400;
    var hero = doc.querySelector('.hero');
    if (hero) {
      triggerY = Math.max(300, hero.offsetHeight - 120);
    }

    function toggle() {
      if ((window.pageYOffset || root.scrollTop) > triggerY) {
        bar.classList.add('is-visible');
      } else {
        bar.classList.remove('is-visible');
      }
    }
    window.addEventListener('scroll', toggle, { passive: true });
    window.addEventListener('resize', function () {
      if (hero) triggerY = Math.max(300, hero.offsetHeight - 120);
      toggle();
    });
    toggle();
  }

  // --------------------------------------------------------------------------
  // Scroll reveal (IntersectionObserver)
  // --------------------------------------------------------------------------
  function initScrollReveal() {
    var nodes = doc.querySelectorAll('[data-reveal]');
    if (!nodes.length) return;

    var prefersReduced =
      window.matchMedia &&
      window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    if (prefersReduced || !('IntersectionObserver' in window)) {
      nodes.forEach(function (n) { n.classList.add('is-visible'); });
      return;
    }

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

    nodes.forEach(function (n) { io.observe(n); });
  }

  // --------------------------------------------------------------------------
  // FAQ: allow only one open at a time per group (optional but feels cleaner)
  // --------------------------------------------------------------------------
  function initFaq() {
    var groups = doc.querySelectorAll('.faq-list');
    groups.forEach(function (group) {
      var items = group.querySelectorAll('.faq-item');
      items.forEach(function (item) {
        item.addEventListener('toggle', function () {
          if (!item.open) return;
          items.forEach(function (other) {
            if (other !== item && other.open) other.open = false;
          });
        });
      });
    });
  }

  // --------------------------------------------------------------------------
  // Bootstrap
  // --------------------------------------------------------------------------
  function boot() {
    initProgressBar();
    initBackToTop();
    initMobileCtaBar();
    initScrollReveal();
    initFaq();
  }

  if (doc.readyState === 'loading') {
    doc.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
