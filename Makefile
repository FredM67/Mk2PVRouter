# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?= -j auto --color
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = content
BUILDDIR      = _build

# Hardware submodule asset directories
MAINBOARD_ASSETS = hardware/mainboard/assets
MK2WIFI_ASSETS   = hardware/expansion_boards/mk2Wifi/assets
IMG_DIR          = $(SOURCEDIR)/img

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile copy-assets

# Copy hardware renders into content/img/ before building
copy-assets:
	@if [ -d "$(MAINBOARD_ASSETS)" ]; then \
		cp $(MAINBOARD_ASSETS)/3phaseDiverter-front.png $(IMG_DIR)/mainboard-front.png; \
		cp $(MAINBOARD_ASSETS)/3phaseDiverter-back.png  $(IMG_DIR)/mainboard-back.png; \
		cp $(MAINBOARD_ASSETS)/3phaseDiverter-smd.png   $(IMG_DIR)/mainboard-smd.png; \
		cp $(MAINBOARD_ASSETS)/3phaseDiverter-bare.png  $(IMG_DIR)/mainboard-bare.png; \
	fi
	@if [ -d "$(MK2WIFI_ASSETS)" ]; then \
		cp $(MK2WIFI_ASSETS)/mk2Wifi-front.png $(IMG_DIR)/mk2wifi-front.png; \
		cp $(MK2WIFI_ASSETS)/mk2Wifi-back.png  $(IMG_DIR)/mk2wifi-back.png; \
		cp $(MK2WIFI_ASSETS)/mk2Wifi-smd.png   $(IMG_DIR)/mk2wifi-smd.png; \
		cp $(MK2WIFI_ASSETS)/mk2Wifi-bare.png  $(IMG_DIR)/mk2wifi-bare.png; \
	fi

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile copy-assets
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O) --show-traceback
