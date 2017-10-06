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
  const chronologyDataIds = ['.firstHistory', '.secondHistory', '.thirdHistory', '.fourthHistory'];


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

 let services = new TimelineMax();
 services.to('.servicesListItem', 1, {
  scale: 1
 }, 0.5);

 let flip = new TimelineMax();
 flip
    .to('.work', 1, {rotationY: '360_cw'}, 0.7);

 let fadeInData = new TimelineMax();
 let fadeOutData = new TimelineMax();

 chronologyDataIds.forEach(id => {
    fadeInData.to(id, 1, {opacity: '1'}, '+=3')
    fadeOutData.to(id, 1, {opacity: '0'}, '+=3')
    new ScrollMagic.Scene({
     triggerElement: id,
     triggerHook: 'onEnter',
     offset: -300,
     duration: 500
   })
     .setTween(fadeInData)
     .addIndicators({name: id})
     .addTo(controller);
 });

 new ScrollMagic.Scene({
          duration: 352,    
          triggerElement: '.servicesListItem',
          triggerHook: 0.90,
          reverse: true,
          tweenChanges: true     
      })
      .setTween(services)
      .addIndicators({name: '.servicesListItem'})
      .addTo(controller);   

  new ScrollMagic.Scene({
          duration: 390,    
          triggerElement: '.work',
          triggerHook: 0.8,
          reverse: true,
          tweenChanges: true
      })
      .setTween(flip)
      .addIndicators({name: '.work'})
      .addTo(controller);  
   
  
  $(document).on('click', '.not-follow', openUrlInNewWindow);

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