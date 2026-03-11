// Make figures with class "clickable-img" open full-size image in new tab
(function() {
    function makeImagesClickable() {
        document.querySelectorAll('img.clickable-img').forEach(function(img) {
            img.style.cursor = 'pointer';
            img.title = 'Cliquer pour agrandir';

            img.onclick = function() {
                window.open(img.src, '_blank');
            };
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', makeImagesClickable);
    } else {
        makeImagesClickable();
    }
})();
