# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = _build
PYTHON := $(shell command -v python3 || command -v python)

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

devhtml:
	@$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(BUILDDIR)/html" $(SPHINXOPTS) $(O)

html: devhtml
	@if [ -z "$(PYTHON)" ]; then \
                echo "Python is not available. Please install Python."; \
                exit 1; \
        else \
                echo "Using Python at: $(PYTHON)"; \
                $(PYTHON) postprocess.py; \
        fi


.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
pdf:
	sphinx-build -b pdf . ./_build
	mv ./_build/Python.pdf ./_build/affdo.pdf	
