#encoding: latin1
# energiprogram
## tar upp f�ljande begrepp:
##reserverade ord
##konstanter
##variabler
##datatyper
##lokal variabel
##global variabel
##formell parameter
##anropsparameter
##typkonvertering
##funktionshuvud
##funktionskropp
##funktion med och utan returv�rde
##

import math

def kinetic_energy(m,v):
    return 0.5*m*math.pow(v,2)

def potential_energy(m,h):
    G = 9.82
    return m*G*h

def skriv(e1, e2):
    print "Bollens r�relseenergi = ", e1, "Joule"  # alt + str(e1)
    print "Bollens potentiella energi", e2, "Joule"

svar = raw_input('Ange bollens massa: ')
m = float(svar)

svar = raw_input('Ange bollens h�jd: ')
h = float(svar)

svar = raw_input('Ange bollens hastighet: ')
v = float(svar)

e1 = kinetic_energy(m,v);
e2 = potential_energy(m,h);

skriv(e1,e2)

