// Make Graphviz SVG diagrams clickable to open in new window
(function() {
    function makeGraphvizClickable() {
        console.log('Clickable graphviz script loaded');

        // Find all graphviz divs
        var graphvizDivs = document.querySelectorAll('div.graphviz');
        console.log('Found ' + graphvizDivs.length + ' graphviz divs');

        graphvizDivs.forEach(function(div) {
            var obj = div.querySelector('object[type="image/svg+xml"]');
            if (!obj) {
                console.log('No object found in div');
                return;
            }

            var svgUrl = obj.getAttribute('data');
            console.log('Setting up clickable graphviz:', svgUrl);

            // Style the container
            div.style.cursor = 'pointer';
            div.title = 'Cliquer pour agrandir';

            // Add click handler directly
            div.onclick = function(e) {
                e.preventDefault();
                e.stopPropagation();
                console.log('Graphviz clicked, opening:', svgUrl);
                window.open(svgUrl, '_blank');
                return false;
            };
        });
    }

    // Try multiple times in case of timing issues
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', makeGraphvizClickable);
    } else {
        makeGraphvizClickable();
    }

    // Also try after a short delay
    setTimeout(makeGraphvizClickable, 100);
})();
