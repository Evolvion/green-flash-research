.PHONY: all clean watch

# Build preprint.pdf with BibTeX via latexmk
all: preprint.pdf

preprint.pdf: preprint.tex refs.bib
	latexmk -pdf -bibtex -interaction=nonstopmode preprint.tex

# Continuous build on file change
watch:
	latexmk -pdf -bibtex -pvc preprint.tex

# Clean all auxiliary files and PDF
clean:
	latexmk -C
