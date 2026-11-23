/*
 * Version links keep the current page: the current base URL is replaced by the
 * base URL of the target version. The same page is used if it exists there,
 * otherwise the home page of that version. The check is done on click.
 */
(function () {
  'use strict';

  // Same page in another version, or null if the current page is not under currentBase.
  function samePageTarget(pathname, currentBase, targetBase) {
    if (!currentBase || pathname.indexOf(currentBase) !== 0) {
      return null;
    }
    return targetBase + pathname.slice(currentBase.length);
  }

  function setup() {
    var versions = document.querySelector('.rst-versions[data-current-base]');
    if (!versions) {
      return;
    }
    var currentBase = versions.getAttribute('data-current-base');
    var links = document.querySelectorAll('a[data-base]');
    Array.prototype.forEach.call(links, function (link) {
      link.addEventListener('click', function (event) {
        var targetBase = link.getAttribute('data-base');
        var target = samePageTarget(window.location.pathname, currentBase, targetBase);
        if (target === null) {
          return; // unknown layout: follow the plain link to the home page
        }
        event.preventDefault();
        var suffix = window.location.search + window.location.hash;
        var go = function (ok) {
          window.location.href = ok ? target + suffix : targetBase;
        };
        fetch(target, {method: 'HEAD'}).then(function (r) { go(r.ok); }, function () { go(false); });
      });
    });
  }

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = {samePageTarget: samePageTarget};
  } else if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', setup);
  } else {
    setup();
  }
}());
