.PHONY: all
all: kompendium.pdf

kompendium.pdf: kompendium.tex
kompendium.pdf: ovn1.tex ovn2.tex ovn3.tex


.PHONY: clean
clean:
	${RM} kompendium.pdf


INCLUDE_MAKEFILES=../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
