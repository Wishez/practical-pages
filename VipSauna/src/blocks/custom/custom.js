import lozad from 'lozad';
import Zooming from 'zooming'

$(function() {
  $(document).on('click', '.not-follow', openUrlInNewWindow);
  // Collapse menu
  $(document).on('blur', '#toggle', function() {
       $("#navbar_collapse").collapse('hide');
  });
  // Zoom
  const zooming = new Zooming({
    bgColor: '#212121'
  });

  zooming.listen('.photoContainer__photo');

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
    
   
    lozad('.photoContainer__photo', {
        load: function(el) {
          el.src = el.dataset.src;
          el.onload = function() {
              el.classList.add('fadeIn');
          }
        }
    }).observe()
});// end ready