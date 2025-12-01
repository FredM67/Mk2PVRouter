// Make Graphviz SVG diagrams clickable to open in new window
document.addEventListener('DOMContentLoaded', function() {
    console.log('Clickable graphviz script loaded');

    // Find all graphviz divs
    var graphvizDivs = document.querySelectorAll('div.graphviz');
    console.log('Found ' + graphvizDivs.length + ' graphviz divs');

    graphvizDivs.forEach(function(div) {
        var obj = div.querySelector('object[type="image/svg+xml"]');
        if (!obj) return;

        var svgUrl = obj.getAttribute('data');
        console.log('Setting up clickable graphviz:', svgUrl);

        // Style the container
        div.style.cursor = 'pointer';
        div.style.display = 'inline-block';
        div.title = 'Cliquer pour agrandir';

        // Wrap in a link
        var link = document.createElement('a');
        link.href = svgUrl;
        link.target = '_blank';
        link.style.display = 'block';
        link.style.textDecoration = 'none';

        // Move object into link
        div.parentNode.insertBefore(link, div);
        link.appendChild(div);
    });
});
