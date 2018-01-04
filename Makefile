.PHONY: all
all: kompendium.pdf

kompendium.pdf: kompendium.tex
kompendium.pdf: ovn1.tex ovn2.tex ovn3.tex
kompendium.pdf: O1.py O2.py O3.py


.PHONY: clean
clean:
	${RM} kompendium.pdf


INCLUDE_MAKEFILES=../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
