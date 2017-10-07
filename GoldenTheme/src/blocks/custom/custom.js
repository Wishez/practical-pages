import ScrollMagic from "scrollmagic";
import { TimelineMax, Linear } from "gsap";
import 'scrollmagic/scrollmagic/uncompressed/plugins/debug.addIndicators';
require('scrollmagic/scrollmagic/uncompressed/plugins/animation.gsap');
import AM from 'adaptivemagic';
import U from 'localutils';

$(function() { 
  let parallaxScenes = [];

  // Paralax
  let parallaxController = new ScrollMagic.Controller({
    globalSceneOptions: U.getParallaxBaseOptions()
  });

  const activateParallaxIfNotMobile = () => {
      AM.doBy('xsUp', () => {
        let pConf = U.getParallaxConf();

        U.getDefaultCustoms().forEach(custom => {
           // Creating Scenes
           parallaxScenes.push( new ScrollMagic.Scene({
                    triggerElement: custom.el,
                    ...custom.sceneConf 
                })
                    .setTween(`${custom.el} > div`, {
                      ...pConf,
                      ...custom.tweenConf
                    })
                    // .addIndicators({name: custom.el})
                    .addTo(parallaxController) );
          });
      }); // end AM.doBy
    }; // end activateParallaxIfNotMobile
  
  const destroyParallaxIfMobile = () => {
      AM.doBy('xxs', () => {
           U.destroyScenesIfNeeded(parallaxScenes);
      }); // end AM.doBy
  }; // end destroyParallaxIfMobile

  destroyParallaxIfMobile()
  activateParallaxIfNotMobile();

  $(window).resize(function() {
    // Change Parallax effect by xsUp size.
    // Don't change it when the parallax was set up by xsUp breakpoint.
    activateParallaxIfNotMobile()
     destroyParallaxIfMobile();
  });
  // Init patalax effect.
  

  let controller = new ScrollMagic.Controller();
  let team = new TimelineMax();
  team
      .to('.worker', 1, {
         y: '-=200'
      }, 0.5)

  new ScrollMagic.Scene({
          triggerElement: '.teamList',
          triggerHook: 1,
          duration: 500
      })
      .setTween(team)
      // .addIndicators({name: 'team\'s persons'})
      .addTo(controller);



 // Services
 let services = new TimelineMax();

 services.to('.servicesListItem', 1, {
  scale: 1
 }, 0.5);

 new ScrollMagic.Scene({
          duration: 352,    
          triggerElement: '.servicesListItem',
          triggerHook: 0.90,
          reverse: true,
          tweenChanges: true     
      })
      .setTween(services)
      // .addIndicators({name: '.servicesListItem'})
      .addTo(controller);   

 // Portfolio
 let flip = new TimelineMax();
 flip
    .to('.work', 1, {rotationY: '360_cw'}, 0.7);

 let fadeInData = new TimelineMax();
 let fadeOutData = new TimelineMax();

 U.getChronologyDataIds().forEach(id => {
    fadeInData.to(id, 1, {opacity: '1'}, '+=3')
    fadeOutData.to(id, 1, {opacity: '0'}, '+=3')
    new ScrollMagic.Scene({
     triggerElement: id,
     triggerHook: 0.75,
     offset: -500,
     duration: 500
   })
     .setTween(fadeInData)
     // .addIndicators({name: id})
     .addTo(controller);
 });


  new ScrollMagic.Scene({
          duration: 390,    
          triggerElement: '.work',
          triggerHook: 0.8,
          reverse: true,
          tweenChanges: true
      })
      .setTween(flip)
      // .addIndicators({name: '.work'})
      .addTo(controller);  
   
  
  $(document)
    .on('click', '.not-follow', openUrlInNewWindow) // end on
    .on('click', '#connectMe', function() {
      const scrollTo = $($(this).data('href')).offset().top;
      
      $('body, html').animate({
          scrollTop: scrollTo
      }, 1500, Linear.ease);
      window.scrollTop
    }) 
    .on('submit', '#connectForm', function(e) { 
        let $this = $(this);

        $this.html('<p class="text-center" style="color: #f1f1f1; font-size: 1.2em;">We have got it!</p>');

        const data = new FormData($this)
        // console.log(data.getAll(), data);

        e.preventDefault();
        return false;
    }); // end on

  $('.curtain')
    .css('width', 0)
    .find('.sk-double-bounce')
    .css('opacity', 0); // end preload

  function openUrlInNewWindow(e) {
    e.preventDefault();
    
    let $target = $(e.target);
    $target = $target[0].tagName === 'A' ? $target : $target.parent();
      
    let url = $target.prop('href');
    
    window.open(url);
  } // end openUrlInNewWindow

});// end ready