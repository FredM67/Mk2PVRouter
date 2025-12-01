// Make Graphviz SVG diagrams clickable to open in new window
(function() {
    function makeGraphvizClickable() {
        document.querySelectorAll('div.graphviz').forEach(function(div) {
            var obj = div.querySelector('object[type="image/svg+xml"]');
            if (!obj) return;

            var svgUrl = obj.getAttribute('data');

            div.style.cursor = 'pointer';
            div.title = 'Cliquer pour agrandir';
            obj.style.pointerEvents = 'none';

            div.onclick = function() {
                window.open(svgUrl, '_blank');
            };
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', makeGraphvizClickable);
    } else {
        makeGraphvizClickable();
    }
})();
