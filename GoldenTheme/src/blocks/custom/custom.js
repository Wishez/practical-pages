// const ScrollMagic = require('scrollmagic');
import ScrollMagic from "scrollmagic";
import { TimelineMax, Linear } from "gsap";
import 'scrollmagic/scrollmagic/uncompressed/plugins/debug.addIndicators'
require('scrollmagic/scrollmagic/uncompressed/plugins/animation.gsap');
// import 'imports?define=>false!scrollmagic/scrollmagic/uncompressed/plugins/animation.gsap';
// import 'scrollmagic/scrollmagic/uncompressed/plugins/adimation.gsap';
// "scrollmagic": "./node_modules/scrollmagic/scrollmagic/uncompressed/ScrollMagic.js"
// ,
    // "scrollmagic": {
    //     "exports": "scrollmagic",
    //     "depends": [
    //         "./node_modules/scrollmagic/scrollmagic/uncompressed/plugins/debug.addIndicators.js",
    //         "./node_modules/scrollmagic/scrollmagic/uncompressed/plugins/animation.gsap.js",
    //         "./node_modules/scrollmagic/scrollmagic/uncompressed/plugins/jquery.ScrollMagic.js"
    //      ]
    // },

$(window).resize(() => {

    let $navList = $('#navList');
    if (window.innerWidth > 799) {
      $navList.show('fast');
    } else  {
      $navList.hide('fast');
    }
});

$(function() {
  const parallaxConf = {y: "80%", ease: Linear.easeNone};
  const baseOptions =  {
    triggerHook: 'onLeave',
    duration: '200%'
  }
  const customs = [
    {el: '#header' , tweenConf: {}, sceneConf: {}},
    {el:'#services' , tweenConf: {}, sceneConf: {}},
    {el:'#portfolio', tweenConf: {}, sceneConf: {}}, 
    {el: '#about', tweenConf: {y: '10%'}, sceneConf: {}}, 
    {el: '#team', tweenConf: {y: '40%'}, sceneConf: {}},
    {el: '#connect', tweenConf: {y: '30%'}, sceneConf: {triggerHook: 'onEnter'}}, 
    {el: '#customers', tweenConf: {}, sceneConf: {duration: '250px'}}
  ];

  let parallaxController = new ScrollMagic.Controller({globalSceneOptions: baseOptions});

  customs.forEach(custom => {
     new ScrollMagic.Scene({
          triggerElement: custom.el,
          ...custom.sceneConf 
      })
      .setTween(`${custom.el} > div`, {
        ...parallaxConf,
        ...custom.tweenConf
      })
      .addIndicators({name: custom.el})
      .addTo(parallaxController);
  })
  
 let controller = new ScrollMagic.Controller();
 let tl = new TimelineMax();
 tl.to('.servicesListItem', 1, {
  scale: 1
 }, 0.5);
 tl.to('.work', 1, {rotationY: '360_cw'}, 0.8)
 new ScrollMagic.Scene({
          duration: 352,    
          triggerElement: '.servicesListItem',
          triggerHook: 0.90,
          reverse: true     
      })
      .setTween(tl)
      .addIndicators({name: '.servicesListItem'})
      .addTo(controller);   

  new ScrollMagic.Scene({
          duration: 399,    
          triggerElement: '.work',
          triggerHook: 0.90,
          reverse: true     
      })
      .setTween(tl)
      .addIndicators({name: '.work'})
      .addTo(controller);  

  $(document).on('click', '.not-follow', openUrlInNewWindow);
  $('.chronologyData').each(function(){
    
     new ScrollMagic.Scene({
       triggerElement: this,
       triggerElement: 0.5
     })
     .setClassToggle(this, 'fade-in')
     .addTo(controller);
  });
  $('.curtain')
    .css('width', 0)
    .find('.sk-double-bounce')
    .css('opacity', 0);
  function openUrlInNewWindow(e) {
    e.preventDefault();
    
    let $target = $(e.target);
    $target = $target[0].tagName === 'A' ? $target : $target.parent();
      
    let url = $target.prop('href');
    
    window.open(url);
  }// end openUrlInNewWindow

});// end ready