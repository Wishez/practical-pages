(function(root, factory) {
  if (typeof define === 'function' && defined.amd) {
    define(factory);
  } else if (typeof exports === 'object'){
    module.exports = factory()
  } else {
    root.U  = factory();
  }
})((window || {}), function() {
  let U = {};
 // Don't change the order
  const _defaultCustoms = [
        {el: '#header' , tweenConf: {}, sceneConf: {}, scene: {}},
        {el:'#services' , tweenConf: {}, sceneConf: {}, scene: {}},
        {el:'#portfolio', tweenConf: {y: "25%"}, sceneConf: {}, scene: {}}, 
        {el: '#about', tweenConf: {y: '10%'}, sceneConf: {}, scene: {}}, 
        {el: '#team', tweenConf: {y: '40%'}, sceneConf: {}, scene: {}},
        {el: '#customers', tweenConf: {}, sceneConf: {duration: '250px'}, scene: {}},
        {el: '#connect', tweenConf: {y: '30%'}, sceneConf: {triggerHook: 'onEnter'}, scene: {}}
  ];
  const _parallaxConf = {y: "50%", ease: Linear.easeNone};
  let _baseOptions =  {
    triggerHook: 'onLeave',
    duration: '200%'
  };
 const _chronologyDataIds = [
      '.firstHistory', 
      '.secondHistory', 
      '.thirdHistory', 
      '.fourthHistory'
  ];
  U.getChronologyDataIds = () => _chronologyDataIds;

  U.getParallaxConf = () => _parallaxConf;
  U.getParallaxBaseOptions = () => _baseOptions;

  U.getDefaultCustoms = () => _defaultCustoms;

  U.isEmptyObject = object  => (
    Object.keys(object).length === 0 && 
    object.constructor === Object
  );

  U.destroyScenesIfNeeded = scenes => {
    scenes.forEach(scene => {
       if (!U.isEmptyObject(scene)) {
          scene.destroy(true);
       }
    });
  }

  return U;
});