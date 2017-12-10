import lozad from 'lozad';
(function() {

  $(function() {
    // Закрытие меню.
    $('#openMenuButton').on('blur', function() {
      $('#navbar_collapse').collapse('hide');
    });
    // Открытие новой вкладки
    $(document).on('click', '.not-follow', openUrlInNewWindow);
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
      // $(window).on('click', '#connectMe', function() {
      //   const scrollTo = $($(this).data('href')).offset().top;
        
      //   $('body, html').animate({
      //       scrollTop: scrollTo
      //   }, 1500, Linear.ease);
      // });
      // 
      // Ленивая загрузка
      lozad('.fadeOut', {
          load: function(el) {
            el.src = el.dataset.src;
            el.onload = function() {
                el.classList.add('fadeIn');
            }
          }
      }).observe();
      // Слайдер
      const $slider = $('#presentation');
      $slider.css('opacity', '0');
      setTimeout(function() {
          $('#presentation').slick({
                slidesToShow: 4,
                slidesToScroll: 1,
                arrows: true,
                infinite:false,
                responsive: [
                  {
                    breakpoint: 1199,
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
                      infinite: true,
                      arrows: false
                    }
                  },
                  {
                    breakpoint: 480,
                    settings: {
                      slidesToShow: 1,
                      slidesToScroll: 1,
                      arrows: false
                    }
                  }
                ]

              });
          $slider.animate({opacity: 1}, 700);
      }, 2500)
      
      // Поп-ап слайдер
      lightbox.option({
        wrapAround: true,
        albumLabel: '%1 изображение из %2',
        fadeDuration: 300,
        imageFadeDuration: 300
      });
  });// end ready
  
}()); // end module