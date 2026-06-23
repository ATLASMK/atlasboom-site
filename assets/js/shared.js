/* Atlas Boom — shared shell behaviour (nav + mobile menu) */
(function(){
  "use strict";
  var nav = document.getElementById('nav');
  if(nav){
    function onScroll(){ nav.classList.toggle('scrolled', window.scrollY > 30); }
    onScroll();
    window.addEventListener('scroll', onScroll, {passive:true});
  }
  var burger = document.getElementById('burger'), mm = document.getElementById('mobileMenu');
  if(burger && mm){
    burger.addEventListener('click', function(){
      var open = mm.classList.toggle('open');
      burger.classList.toggle('open', open);
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
      document.body.style.overflow = open ? 'hidden' : '';
    });
    mm.querySelectorAll('a').forEach(function(a){
      a.addEventListener('click', function(){
        mm.classList.remove('open'); burger.classList.remove('open');
        burger.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      });
    });
  }
})();
