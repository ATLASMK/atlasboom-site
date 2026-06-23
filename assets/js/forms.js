/* Atlas Boom — shared form handler (Web3Forms + mailto: fallback)
   Forms opt in by adding `data-atlas-form` + `data-subject="..."`.
   When WEB3FORMS_ACCESS_KEY is empty, every form falls back to mailto: so
   the site still works the day a fresh user clones the repo. */
(function(){
  // To activate POST-by-fetch submissions:
  //   1. Sign up free at https://web3forms.com/ with info@atlasboom.com
  //   2. Paste the access key (free tier = 250 submissions/month).
  //   3. No other change needed.
  var WEB3FORMS_ACCESS_KEY = "";
  var ENDPOINT = "https://api.web3forms.com/submit";
  var FALLBACK_EMAIL = "info@atlasboom.com";

  function mailtoUrl(form, subject){
    var lines = [];
    var els = form.querySelectorAll('input,select,textarea');
    for(var i=0; i<els.length; i++){
      var el = els[i];
      if(!el.name || el.name === 'access_key' || el.type === 'submit' || el.type === 'button') continue;
      lines.push(el.name + ': ' + (el.value || '(none)'));
    }
    return 'mailto:' + FALLBACK_EMAIL +
           '?subject=' + encodeURIComponent(subject) +
           '&body=' + encodeURIComponent(lines.join('\n'));
  }

  function reveal(form){
    var success = form.parentElement.querySelector('.success');
    if(success){
      form.style.display = 'none';
      success.classList.add('show');
    }
  }

  function send(form, e){
    e.preventDefault();
    if(!form.checkValidity()){ form.reportValidity(); return; }
    var subject = form.dataset.subject || 'Atlas Boom website request';

    // No key configured: mailto: opens immediately.
    if(!WEB3FORMS_ACCESS_KEY){
      window.location.href = mailtoUrl(form, subject);
      reveal(form);
      return;
    }

    // Key set: fetch POST, fall back to mailto: on any failure.
    var btn = form.querySelector('button[type=submit]');
    var oldLabel = btn ? btn.textContent : '';
    if(btn){ btn.textContent = 'Sending...'; btn.disabled = true; }

    var data = new FormData(form);
    data.set('access_key', WEB3FORMS_ACCESS_KEY);
    data.set('subject', subject);
    data.set('from_name', 'Atlas Boom website');

    fetch(ENDPOINT, { method:'POST', body:data })
      .then(function(r){ return r.json(); })
      .then(function(d){
        if(d && d.success){
          reveal(form);
        } else {
          window.location.href = mailtoUrl(form, subject);
          reveal(form);
        }
      })
      .catch(function(){
        window.location.href = mailtoUrl(form, subject);
        reveal(form);
      })
      .then(function(){
        if(btn){ btn.textContent = oldLabel; btn.disabled = false; }
      });
  }

  var forms = document.querySelectorAll('form[data-atlas-form]');
  for(var i=0; i<forms.length; i++){
    (function(f){
      f.addEventListener('submit', function(e){ send(f, e); });
    })(forms[i]);
  }
})();
