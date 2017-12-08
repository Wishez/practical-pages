import lozad from 'lozad';

$(function() {
  $(document).on('click', '.not-follow', openUrlInNewWindow);
  $('#openMenuButton').on('blur', function() {
    $('#navbar_collapse').collapse('hide');
  });
  function openUrlInNewWindow(e) {
    e.preventDefault();
    
    let $target = $(e.target);
    $target = $target[0].tagName === 'A' ? $target : $target.parent();
      
    let url = $target.prop('href');
    
    window.open(url);
  }// end openUrlInNewWindow
  
  // Preload
  $('.curtain')
    .css('width', 0)
    .find('.sk-cube-grid')
    .css('opacity', 0); // end preload
    
    // For scroll
    $(window).on('click', '#connectMe', function() {
      const scrollTo = $($(this).data('href')).offset().top;
      
      $('body, html').animate({
          scrollTop: scrollTo
      }, 1500, Linear.ease);
      window.scrollTop
    });
     lozad('.fadeOut', {
        load: function(el) {
          el.src = el.dataset.src;
          el.onload = function() {
              el.classList.add('fadeIn');
          }
        }
    }).observe();

    $('#presentation').slick({
      slidesToShow: 4,
      arrows: true,
      infinite:false,
      responsive: [
        {
          breakpoint: 992,
          settings: {
            slidesToShow: 3,
            slidesToScroll: 1,
            infinite: true
          }
        },
        {
          breakpoint: 768,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 1,
            infinite: true
          }
        },
        {
          breakpoint: 480,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1
          }
        }
      ]

    });

    lightbox.option({
      wrapAround: true,
      albumLabel: '%1 изображение из %2',
      fadeDuration: 300,
      imageFadeDuration: 300
    });
});// end ready