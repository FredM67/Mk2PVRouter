# The image the documentation workflow builds in: everything it installs, done
# once. The workflow tags it with the month and a hash of this file and of
# requirements.txt, so it is rebuilt when either changes, and once a month
# (a newer drawio, Debian updates).
#
# Debian trixie with Python 3.14, as the devcontainer: weasyprint (PDF)
# segfaults on ubuntu-26.04, the system of ubuntu-latest.
FROM python:3.14-trixie

LABEL org.opencontainers.image.source="https://github.com/FredM67/Mk2PVRouter"
LABEL org.opencontainers.image.description="Build environment of the Mk2PVRouter documentation"

# git-lfs for the checkout; graphviz; xvfb for headless drawio; the
# Pango/HarfBuzz libraries of weasyprint and its fonts (DejaVu, Noto Color
# Emoji for the emojis of the docs, Symbola for the symbols the other two
# lack, such as ⏚ and ⎓); the latest drawio desktop
RUN apt-get update \
    && apt-get install -y --no-install-recommends git-lfs graphviz xvfb libasound2t64 \
       libpango-1.0-0 libpangoft2-1.0-0 libharfbuzz-subset0 \
       fonts-dejavu-core fonts-noto-color-emoji fonts-symbola \
    && ARCH=$(dpkg --print-architecture) \
    && DRAWIO_URL=$(curl -s https://api.github.com/repos/jgraph/drawio-desktop/releases/latest \
       | grep browser_download_url | grep "${ARCH}" | grep '\.deb' | head -1 | cut -d '"' -f 4) \
    && curl -fLo /tmp/drawio.deb "$DRAWIO_URL" \
    && apt-get install -y /tmp/drawio.deb \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/drawio.deb

COPY requirements.txt /tmp/requirements.txt
RUN python -m pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt
