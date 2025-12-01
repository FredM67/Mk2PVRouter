// Make Graphviz SVG diagrams clickable to open in new window
document.addEventListener('DOMContentLoaded', function() {
    // Find all graphviz object elements
    var graphvizObjects = document.querySelectorAll('.graphviz object[type="image/svg+xml"]');

    graphvizObjects.forEach(function(obj) {
        // Make the container clickable
        obj.style.cursor = 'zoom-in';
        obj.parentElement.style.cursor = 'zoom-in';

        // Add click handler to open SVG in new tab
        var clickHandler = function(e) {
            e.preventDefault();
            var svgUrl = obj.data;
            if (svgUrl) {
                window.open(svgUrl, '_blank');
            }
        };

        obj.addEventListener('click', clickHandler);
        obj.parentElement.addEventListener('click', clickHandler);
    });
});
