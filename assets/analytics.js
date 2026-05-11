/*
 * Hoffman Legal — Call / Free Consultation click tracking.
 *
 * Fires GA4 events (via the gtag() loaded in the page head) when a visitor
 * taps any phone link or Free Consultation CTA. Also captures which practice
 * area page the click happened on, so the event can be filtered by page in
 * GA4 Reports -> Engagement -> Events.
 *
 * Event names:
 *   - click_call             — any phone link
 *   - click_free_consultation — any "Free Consultation" / "Free Consult" CTA
 *
 * Event params:
 *   location      — header_desktop | mobile_menu | mobile_sticky | other
 *   practice_area — slug derived from the current HTML filename (e.g. "car-accidents")
 *   page_title    — document.title for context
 */
(function () {
  if (typeof window === 'undefined') return;

  function getPracticeArea() {
    var path = (window.location.pathname || '').split('/').pop() || 'index.html';
    // Strip trailing slash / query / hash if the URL is odd.
    path = path.replace(/[?#].*$/, '');
    if (!path || path === '/') path = 'index.html';
    return path.replace(/\.html?$/i, '') || 'index';
  }

  function locationFor(el) {
    if (el.closest('.mobile-cta-bar')) return 'mobile_sticky';
    if (el.closest('.mobile-menu') || el.closest('.mobile-cta-container')) return 'mobile_menu';
    if (el.closest('.header') || el.closest('.nav-desktop')) return 'header_desktop';
    return 'other';
  }

  function track(eventName, el) {
    if (typeof window.gtag !== 'function') return;
    try {
      window.gtag('event', eventName, {
        location: locationFor(el),
        practice_area: getPracticeArea(),
        page_title: document.title || ''
      });
    } catch (_) {
      /* swallow — analytics must never break the site */
    }
  }

  // Call selectors: any tel: link, plus the specific call classes used site-wide.
  var CALL_SELECTOR = 'a[href^="tel:"], .nav-phone, .mobile-phone, .mcb-call';
  // Consultation selectors: every flavor of the Free Consultation button.
  var CONSULT_SELECTOR = '.nav-cta, .mobile-cta, .mcb-consult';

  function bind() {
    document.addEventListener('click', function (e) {
      var target = e.target;
      if (!target || !target.closest) return;
      var callEl = target.closest(CALL_SELECTOR);
      if (callEl) {
        track('click_call', callEl);
        return;
      }
      var consultEl = target.closest(CONSULT_SELECTOR);
      if (consultEl) {
        track('click_free_consultation', consultEl);
      }
    }, true); // capture phase so we record before navigation
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', bind);
  } else {
    bind();
  }
})();
