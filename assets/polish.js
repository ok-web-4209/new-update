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
  //   Always visible on mobile the moment the page loads (no scroll needed).
  //   Auto-hides while the mobile menu overlay is open so the two don't collide
  //   visually — the menu has its own phone + consult links further up.
  // --------------------------------------------------------------------------
  function initMobileCtaBar() {
    var bar = doc.querySelector('.mobile-cta-bar');
    if (!bar) return;

    body.classList.add('has-mobile-cta');
    // Show immediately; CSS media query keeps it desktop-hidden.
    bar.classList.add('is-visible');

    // Watch the mobile menu for open/close so we can slide the bar out of the
    // way while it's open. Works on every page because they all use the same
    // `#mobileMenu` element and `.open` class.
    var menu = doc.getElementById('mobileMenu');
    if (!menu) return;

    function syncMenuState() {
      if (menu.classList.contains('open')) {
        body.classList.add('menu-open');
      } else {
        body.classList.remove('menu-open');
      }
    }

    if ('MutationObserver' in window) {
      var mo = new MutationObserver(syncMenuState);
      mo.observe(menu, { attributes: true, attributeFilter: ['class'] });
    }
    syncMenuState();
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
