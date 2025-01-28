
(function() {
  "use strict";

  /**
   * Apply .scrolled class to the body as the page is scrolled down
   */
  function toggleScrolled() {
      const selectBody = document.querySelector('body');
      const selectHeader = document.querySelector('#header');
      if (!selectHeader.classList.contains('scroll-up-sticky') 
          && !selectHeader.classList.contains('sticky-top') 
          && !selectHeader.classList.contains('fixed-top')) 
          return;
      let selectHero = document.querySelector('.hero');
      let threshold = selectHero.clientHeight - selectHeader.clientHeight
      if (window.scrollY > 50) {
        selectBody.classList.add('scrolled');
        if (window.scrollY > threshold) {
          selectBody.classList.add('scrolled-light');
        } else {
          selectBody.classList.remove('scrolled-light');
        }

      } else {
        selectBody.classList.remove('scrolled');
      }
  }

  document.addEventListener('scroll', toggleScrolled);
  window.addEventListener('load', toggleScrolled);


  /**
   * Desktop nav toggle
   */
  // document.querySelectorAll('.dropdown').forEach(dropdownBtn => {
  //   dropdownBtn.addEventListener('click', dropdownToggle)
  // });

  // function dropdownToggle(e) {
  //   e.preventDefault();
  //   this.classList.toggle('active');
  //   const selectBody = document.querySelector('body');
  //   if (this.classList.contains('active')) {
  //     selectBody.addEventListener('click', dropdownCollapse);
  //   } else {
  //     selectBody.removeEventListener('click', dropdownCollapse);
  //   }
  //   e.stopImmediatePropagation();
  // }

  // function dropdownCollapse(e) {
  //   e.preventDefault();
  //   document.querySelectorAll('.dropdown.active').forEach(dropdownBtn => {
  //     dropdownBtn.classList.toggle('active')
  //   });    
  //   e.stopImmediatePropagation();
  // }

  /**
   * Mobile nav toggle
   */
  const mobileNavToggleBtn = document.querySelector('.mobile-nav-toggle');

  function mobileNavToogle() {
    document.querySelector('body').classList.toggle('mobile-nav-active');
    mobileNavToggleBtn.classList.toggle('bi-list');
    mobileNavToggleBtn.classList.toggle('bi-x');
  }
  mobileNavToggleBtn.addEventListener('click', mobileNavToogle);

  /**
   * Hide mobile nav on same-page/hash links
   */
  document.querySelectorAll('.nav-menu a').forEach(navmenu => {
    navmenu.addEventListener('click', () => {
      if (document.querySelector('.mobile-nav-active')) {
        mobileNavToogle();
      }
    });

  });

  /**
   * Toggle mobile nav dropdowns
   */
  document.querySelectorAll('.nav-menu .toggle-dropdown').forEach(navmenu => {
    navmenu.addEventListener('click', function(e) {
      e.preventDefault();
      this.parentNode.classList.toggle('active');
      this.parentNode.nextElementSibling.classList.toggle('dropdown-active');
      if (document.querySelector('.mobile-nav-active')) {
        e.stopImmediatePropagation();
      }
    });
  });


  /**
   * Auto generate the carousel indicators
   */
  document.querySelectorAll('.carousel-indicators').forEach((carouselIndicator) => {
    carouselIndicator.closest('.carousel').querySelectorAll('.carousel-item').forEach((carouselItem, index) => {
      if (index === 0) {
        carouselIndicator.innerHTML += `<li data-bs-target="#${carouselIndicator.closest('.carousel').id}" data-bs-slide-to="${index}" class="active"></li>`;
      } else {
        carouselIndicator.innerHTML += `<li data-bs-target="#${carouselIndicator.closest('.carousel').id}" data-bs-slide-to="${index}"></li>`;
      }
    });
  });

  
  /**
   * Preloader system
   */
  

  /**
   * Scroll top button
   */
  let scrollTop = document.querySelector('.scroll-top');

  function toggleScrollTop() {
    if (scrollTop) {
      window.scrollY > 100 ? scrollTop.classList.add('active') : scrollTop.classList.remove('active');
    }
  }
  scrollTop.addEventListener('click', (e) => {
    e.preventDefault();
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });

  window.addEventListener('load', toggleScrollTop);
  document.addEventListener('scroll', toggleScrollTop);

  /**
   * Animation on scroll function and init
   */
  function aosInit() {
    AOS.init({
      duration: 600,
      easing: 'ease-in-out',
      once: true,
      mirror: false
    });
  }
  window.addEventListener('load', aosInit);

  

  /**
   * Initiate glightbox
   */
  const glightbox = GLightbox({
    selector: '.glightbox'
  });

  /**
   * Initiate Pure Counter
   */
  new PureCounter();

  /**
   * Init isotope layout and filters
   */
  document.querySelectorAll('.isotope-layout').forEach(function(isotopeItem) {
    let layout = isotopeItem.getAttribute('data-layout') ?? 'masonry';
    let filter = isotopeItem.getAttribute('data-default-filter') ?? '*';
    let sort = isotopeItem.getAttribute('data-sort') ?? 'original-order';

    let initIsotope;
    imagesLoaded(isotopeItem.querySelector('.isotope-container'), function() {
      initIsotope = new Isotope(isotopeItem.querySelector('.isotope-container'), {
        itemSelector: '.isotope-item',
        layoutMode: layout,
        filter: filter,
        sortBy: sort
      });
    });

    isotopeItem.querySelectorAll('.isotope-filters li').forEach(function(filters) {
      filters.addEventListener('click', function() {
        isotopeItem.querySelector('.isotope-filters .filter-active').classList.remove('filter-active');
        this.classList.add('filter-active');
        initIsotope.arrange({
          filter: this.getAttribute('data-filter')
        });
        if (typeof aosInit === 'function') {
          aosInit();
        }
      }, false);
    });

  });

  /**
   * Init swiper sliders
   */
  function initSwiper() {
    document.querySelectorAll(".init-swiper").forEach(function(swiperElement) {
      let config = JSON.parse(
        swiperElement.querySelector(".swiper-config").innerHTML.trim()
      );

      if (swiperElement.classList.contains("swiper-tab")) {
        initSwiperWithCustomPagination(swiperElement, config);
      } else {
        new Swiper(swiperElement, config);
      }
    });
  }

  window.addEventListener("load", initSwiper);

  /**
   * Correct scrolling position upon page load for URLs containing hash links.
   */
  window.addEventListener('load', function(e) {
    if (window.location.hash) {
      if (document.querySelector(window.location.hash)) {
        setTimeout(() => {
          let section = document.querySelector(window.location.hash);
          let scrollMarginTop = getComputedStyle(section).scrollMarginTop;
          window.scrollTo({
            top: section.offsetTop - parseInt(scrollMarginTop),
            behavior: 'smooth'
          });
        }, 100);
      }
    }
  });

  /**
   * Navmenu Scrollspy
   */
  let navmenulinks = document.querySelectorAll('.navmenu a');

  function navmenuScrollspy() {
    navmenulinks.forEach(navmenulink => {
      if (!navmenulink.hash) return;
      let section = document.querySelector(navmenulink.hash);
      if (!section) return;
      let position = window.scrollY + 200;
      if (position >= section.offsetTop && position <= (section.offsetTop + section.offsetHeight)) {
        document.querySelectorAll('.navmenu a.active').forEach(link => link.classList.remove('active'));
        navmenulink.classList.add('active');
      } else {
        navmenulink.classList.remove('active');
      }
    })
  }
  window.addEventListener('load', navmenuScrollspy);
  document.addEventListener('scroll', navmenuScrollspy);

  /**
   * Navmenu Active Link
   */
  let bodyId = document.querySelector('body').id;
  if (bodyId) {
    let targetMenuLink = document.getElementById(`${bodyId}-link`);
    if (targetMenuLink) {
      targetMenuLink.classList.add('active');
      // targetMenuLink.href = '#'
    }
  }

  /**
   * Section Animation
   */

  function addFadeUp(elt, delay) {
    elt.setAttribute('data-aos', 'fade-up');
    elt.setAttribute('data-aos-delay', delay)
  }

  document.querySelectorAll('.section-title').forEach(content => addFadeUp(content, '50'));
  document.querySelectorAll('.coming-soon-content').forEach(content => addFadeUp(content, '100'));
  document.querySelectorAll('.about-content').forEach(content => addFadeUp(content, '100'));
  document.querySelectorAll('.speech-content').forEach(content => addFadeUp(content, '200'));
  document.querySelectorAll('.speech-author').forEach(content => addFadeUp(content, '200'));
  document.querySelectorAll('.stats-item').forEach(content => addFadeUp(content, '100'));
  document.querySelectorAll('.features-item').forEach(content => addFadeUp(content, '100'));
  document.querySelectorAll('.news-item').forEach(content => addFadeUp(content, '100'));
  document.querySelectorAll('.news-footer').forEach(content => addFadeUp(content, '100'));

})();