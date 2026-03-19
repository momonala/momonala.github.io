(function($) {
  "use strict"; // Start of use strict

  var SCROLL_ANIMATION_DURATION_MS = 1000;

  function handleSmoothScroll(event) {
    var targetHash = this.hash;
    if (!targetHash) {
      return;
    }

    if (location.pathname.replace(/^\//, '') === this.pathname.replace(/^\//, '') &&
        location.hostname === this.hostname) {
      var target = $(targetHash);
      target = target.length ? target : $('[name=' + targetHash.slice(1) + ']');
      if (target.length) {
        event.preventDefault();
        event.stopPropagation();

        $('html, body').animate(
          {
            scrollTop: (target.offset().top)
          },
          SCROLL_ANIMATION_DURATION_MS,
          "easeInOutExpo"
        );
      }
    }
  }

  function handleNavCollapse() {
    $('.navbar-collapse').collapse('hide');
  }

  // Smooth scrolling using jQuery easing
  $('a.js-scroll-trigger[href*="#"]:not([href="#"])').on('click', handleSmoothScroll);

  // Closes responsive menu when a scroll trigger link is clicked
  $('.js-scroll-trigger').on('click', handleNavCollapse);

  // Activate scrollspy to add active class to navbar items on scroll
  $('body').scrollspy({
    target: '#sideNav'
  });

})(jQuery); // End of use strict
