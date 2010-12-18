#encoding: latin1

class Produkt:

    def __init__(self, beskrivning, pris):
        self.__beskrivning = beskrivning
        self.__pris = pris

    def beskrivning(self):
        return self.__beskrivning

    def pris(self):
        return self.pris

    def __cmp__(self, other):
        if self.__pris > other.__pris:
            return 1
        elif self.__pris < other.__pris:
            return -1
        else:
            return 0

    def __str__(self):
        return 'Beskrivning: ' + self.__beskrivning +'\n' + 'Pris: ' + str(self.__pris) 


class Kund:

    def __init__(self, fnamn, enamn):
        self.__fnamn = fnamn
        self.__enamn = enamn
        self.__produkter = list()

    def addera(self, produkt):
        self.__produkter.append(produkt)

    def radera(self, produkt):
		for p in self.__produkter:
			if p.beskrivning() == produkt.beskrivning:
				pass
				break

    def fnamn(self):
        return self.__fnamn

    def enamn(self):
        return self.__enamn

    def produkter(self):
        return self.__produkter

    def __cmp__(self, other):
        if self.__fnamn > other.__fnamn:
            return 1
        elif self.__fnamn < other.__fnamn:
            return -1
        else:
            return 0

    def __str__(self):
        return 'Förnamn: ' + self.__fnamn +'\n' + 'Efternamn: ' + str(self.__enamn) 




p1 = Produkt('Omega-3',99)
p2 = Produkt('Mellanmjölk',10)
p3 = Produkt('Banan',5)
produkterna = [p1, p2, p3]

produkterna.sort()
for p in produkterna:
    print p

k1 = Kund('Sten', 'Andersson')
k2 = Kund('Ada', 'Adamsson')
k3 = Kund('Beda', 'Bengtsson')
k1.addera(p1)
k2.addera(p2)
k3.addera(p3)
kunderna = [k1, k2, k3]

kunderna.sort()
for k in kunderna:
    print k

