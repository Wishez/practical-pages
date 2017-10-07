/* */


(function ( root, factory ) {
     if ( typeof define === 'function' && define.amd ) {
      // AMD. Register as an anonymous module.
        define( factory );
    } else if ( typeof exports === 'object' ) {
      // CommonJS
      module.exports = factory();
    } else {
      // Browser global
      root.AM = factory();
    }
})((window || {}), function() {

  let AdaptiveMagic = {};
  
  let _breakpoints = {
    lgLess: 1600,
    lg: {
      min: 1600,
      max: 1199
    },
    lgUp: 1199,
    mdLess: 1200,
    md: {
      min: 991,
      max: 1200
    },
    mdUp: 991,
    smLess: 992,
    sm: {
      min: 799,
      max: 992
    },
    smUp: 799,
    xsLess: 800,
    xs: {
      min: 560,
      max: 800
    },
    xsUp: 559,
    xxs: 560,
    xxsUp: 0
  };

  let _defaultLimitations = {
        lg: false,
        md: false,
        sm: false,
        xs: false,
        xxs: false,
        lgLess: false,
        mdLess: false,
        smLess: false,
        xsLess: false,
        xxsLess: false,
        lgUp: false,
        mdUp: false,
        smUp: false,
        xsUp: false,
        xxsUp: false
  };

  AdaptiveMagic.limitations = {
        lastBreakpoint: "",
        isUsingLimitation: true 
  };
  const _assert = ( condition, message ) => {
        if (condition) 
             throw Error(message)
  }
  const _insistentOf = ( value, type ) => typeof value === type;
  const _notEqualOf = ( value, type ) => typeof value !== type;

  // Set value of isUsingLimitation in _limitations object
  // for allow or prevent to repeat action by changing a screen size's width.
  // isLimited: bool
  AdaptiveMagic.changeLimitationMode = isLimited => {
    _assert(
        typeof isLimited !== 'bool',
        'First argument must be a value of Boolean type.'
    );

    _limitations = {
        ...limitations,
        isUsingLimitation: isLimited
    }
  };

  // Check range of window size's width. You can point
  // your range of breakpoint as an object with two 
  // property : {min: num, max: num}
  // or take one of default sizes.
  // Breakpoint: object or string
   const _checkWidth = breakpoint => {
    const screenWidth = window.innerWidth;
    // console.log(breakpoint, screenWidth,_breakpoints.xxs,  screenWidth < _breakpoints.xss);
    // Check the range of breakpoint.
    if ( _insistentOf( breakpoint, 'object' ) ) {
        // Range of size
        if ( _breakpoints.min && _breakpoints.max ) {
            return (screenWidth > _breakpoints.min && 
                         screenWidth < _breakpoints.max);
        } else if ( _breakpoints.min ) {
            // Less than
            return screenWidth > _breakpoints.min;
        } else { 
            // Up than
            return screenWidth < _breakpoints.max
        }
    }

    switch ( breakpoint ) {
      // Up than
      case 'lgUp':
        return screenWidth > _breakpoints.lgUp;
      case 'mdUp':
        return screenWidth > _breakpoints.mdUp;
      case 'smUp':
        return screenWidth > _breakpoints.smUp;
      case 'xsUp':
        return screenWidth > _breakpoints.xsUp;
      // Less and more than 
      case 'lg':
        return (screenWidth > _breakpoints.lg.min &&
                     screenWidth < _breakpoints.lg.max);
      case 'md':
        return ( screenWidth > _breakpoints.md.min && 
                      screenWidth < _breakpoints.md.max);
      case 'sm':
        return ( screenWidth > _breakpoints.sm.min && 
                      screenWidth < _breakpoints.sm.max);
      case 'xs':
        return ( screenWidth > _breakpoints.xs.min && 
                      screenWidth < _breakpoints.xs.max);
      // Less than
      case 'lgLess':
        return screenWidth < _breakpoints.lgLess;
      case 'mdLess':
        return screenWidth < _breakpoints.mdLess;
      case 'smLess':
        return screenWidth < _breakpoints.smLess;
      case 'xsLess':
        return screenWidth < _breakpoints.xsLess;
      case 'xxs':
        return screenWidth < _breakpoints.xxs;
      // If a breakpoint wasn't defined.
      default:
        return false;
    };
  };
  const _setLastBreakpointIfNeeded = ( 
      breakpoint,
      isForce = false 
  ) => {
      const lb = AdaptiveMagic.limitations.lastBreakpoint;
      if (!lb || isForce) {
            AdaptiveMagic.limitations.lastBreakpoint = breakpoint;
      } else {
            return false;
      }
  }
  AdaptiveMagic.doBy = (breakpoint, callback) => {

       _assert(
            ( _notEqualOf( breakpoint, 'string' ) && _notEqualOf( breakpoint,  'object' ) ), 
            'First argument must be an object or a string.'
        );
      _setLastBreakpointIfNeeded(breakpoint);
      // If allowed to prevent action AdaptiveMagic is repeated by a breakpoint, 
      // the next iteration won't be repeated by a breakpoint.
      const lastBreakpoint = AdaptiveMagic.limitations.lastBreakpoint;
      let callable = false;
      // I checks a needed breakpoint and check for a last  call of a callback.
      // If there was set isUsingLimitation as false, then callback can repeat.
      if ( ( _checkWidth(breakpoint) && lastBreakpoint !== breakpoint ) || 
          !AdaptiveMagic.limitations.isUsingLimitation )
          callable = true;


      if ( callable) {
        callback();

        if ( AdaptiveMagic.limitations.isUsingLimitation ) {
            _setLastBreakpointIfNeeded(breakpoint, true);
        }
      } 

      console.log('exit');
  };
  AdaptiveMagic.setBreakpoints = breakpoints => {
      _assert( _notEqualOf( breakpoints, 'object' ) );
      _breakpoints = {
        ..._breakpoints,
        ...breakpoints
      };
  };
  
   return AdaptiveMagic;
});