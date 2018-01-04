import math

def kinetic_energy(m, v):
    return 0.5*m*math.pow(v,2)

def potential_energy(m, h):
    G = 9.82
    return m*G*h

def skriv(e1, e2):
    print("Bollens rörelseengergi = " + str(e1) + "Joule")
    print("Bollens potentiella energi" + str(e2) + "Joule")

svar = input('Ange bollens massa: ')
m = float(svar)

svar = input('Ange bollens höjd: ')
h = float(svar)

svar = input('Ange bollens hastighet: ')
v = float(svar)

e1 = kinetic_energy(m,v);
e2 = potential_energy(m,h);

skriv(e1,e2)

