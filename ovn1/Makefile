#include ../Makefile.inc

DOCUMENT=	
TEXFILE=	
DEPS=		


TEX=		latex
PDFTEX=		pdflatex
DVIPS=		dvips
TEXFLAGS=	
MAKEINDEX=	makeindex
BIBTEX=		bibtex


.SUFFIXES: .tex .pdf .ps .dvi
.PHONY: all clean pdf ps publish publish_doc publish_deps struct print


.tex.pdf:
	while (${PDFTEX} ${TEXFLAGS} $<; \
		grep "Rerun to get cross" ${TEXFILE:.tex=.log}) \
		do true; done
.tex.dvi:
	while (${TEX} ${TEXFLAGS} $<; \
		grep "Rerun to get cross" ${TEXFILE:.tex=.log}) \
		do true; done
.dvi.ps:
	${DVIPS} -o $@ $<


all: ${DOCUMENT}

pdf:	${TEXFILE:.tex=.pdf}
ps:	${TEXFILE:.tex=.ps}
dvi:	${TEXFILE:.tex=.dvi}

${DOCUMENT}: ${TEXFILE}
	${PDFTEX} ${TEXFILE}
	-${BIBTEX} ${TEXFILE:.tex=}
	-${MAKEINDEX} ${TEXFILE}
	while (${PDFTEX} ${TEXFLAGS} $<; \
		grep "Rerun to get cross" ${TEXFILE:.tex=.log}) \
		do true; done

${TEXFILE}: ${DEPS}


clean:
	@rm -f *.log *.aux *.toc *.core *.o *~ *.bbl *.blg *.ind *.ilg \
		*.dvi *.ps *.pdf

publish_doc: ${DOCUMENT}
	cp ${DOCUMENT} ${PUBDIR}

publish_deps: ${DEPS}
	cp ${DEPS} ${PUBDIR}

publish: publish_doc publish_deps

struct:
	@echo "No struct defined."

print: ps
	print ${TEXFILE:.tex=.ps}

