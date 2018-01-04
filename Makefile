.PHONY: all
all: kompendium.pdf

kompendium.pdf: kompendium.tex
kompendium.pdf: satser-funktioner/ovn1.tex
kompendium.pdf: satser-funktioner/O1.py
kompendium.pdf: logik-villkor/ovn2.tex
kompendium.pdf: logik-villkor/O2.py
kompendium.pdf: logik-villkor/O2-sten.py


.PHONY: clean
clean:
	${RM} kompendium.pdf


INCLUDE_MAKEFILES=makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
