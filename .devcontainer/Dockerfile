FROM mcr.microsoft.com/devcontainers/python:3.14-trixie

# Graphviz, xvfb (needed for headless DrawIO rendering), and for the PDF
# (make simplepdf): the Pango/HarfBuzz libraries of weasyprint and the fonts
# it uses in CI (DejaVu, Noto Color Emoji for the emojis of the docs)
RUN apt-get update \
    && apt-get install -y --no-install-recommends graphviz xvfb \
       libpango-1.0-0 libpangoft2-1.0-0 libharfbuzz-subset0 \
       fonts-dejavu-core fonts-noto-color-emoji \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install latest DrawIO desktop (same approach as CI workflow)
RUN ARCH=$(dpkg --print-architecture) \
    && DRAWIO_URL=$(curl -s https://api.github.com/repos/jgraph/drawio-desktop/releases/latest \
       | grep browser_download_url | grep "${ARCH}" | grep '\.deb' | head -1 | cut -d '"' -f 4) \
    && curl -Lo /tmp/drawio.deb "$DRAWIO_URL" \
    && apt-get update \
    && apt-get install -y libasound2t64 \
    && apt-get -f install -y /tmp/drawio.deb \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/drawio.deb
