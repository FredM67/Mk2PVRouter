FROM mcr.microsoft.com/devcontainers/python:3.12

# Install Graphviz and xvfb (needed for headless DrawIO rendering)
RUN apt-get update \
    && apt-get install -y --no-install-recommends graphviz xvfb \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install latest DrawIO desktop (same approach as CI workflow)
RUN ARCH=$(dpkg --print-architecture) \
    && DRAWIO_URL=$(curl -s https://api.github.com/repos/jgraph/drawio-desktop/releases/latest \
       | grep browser_download_url | grep "${ARCH}" | grep '\.deb' | head -1 | cut -d '"' -f 4) \
    && curl -Lo /tmp/drawio.deb "$DRAWIO_URL" \
    && apt-get update \
    && apt-get -f install -y /tmp/drawio.deb \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/drawio.deb
