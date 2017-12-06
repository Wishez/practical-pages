$(window).resize(() => {

});

$(function() {
  $(document).on('click', '.not-follow', openUrlInNewWindow);
  $('#openMenuButton').on('blur', function() {
    // $('#navbar_collapse').collapse('hide');
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
    .find('.sk-double-bounce')
    .css('opacity', 0); // end preload
    
    // For scroll
    $(window).on('click', '#connectMe', function() {
      const scrollTo = $($(this).data('href')).offset().top;
      
      $('body, html').animate({
          scrollTop: scrollTo
      }, 1500, Linear.ease);
      window.scrollTop
    }) 
});// end ready