#

class Konto:

    def __init__(self, nr, namn, saldo):
        self.nr = nr
        self.namn = namn
        self.saldo = saldo

    def __str__(self):
        return str(self.nr) + '\n' + self.namn + '\n' + str(self.saldo) + ' kr\n' 

    def deposit(self, amount):
        self.saldo += amount

    def withdraw(self, amount):
        self.saldo -= amount


def lasIn():
    infil = open('infil.txt','r')
    rad = infil.readline()
    kontona = list()
    while rad != '':
        rad = rad.rstrip('\n')
        delar = rad.split('/')
        nr = int(delar[0])
        namn = delar[1]
        saldo = float(delar[2])
        tmp = Konto(nr,namn,saldo)
        kontona.append(tmp)
        rad = infil.readline()
    return kontona

def skrivUt(kontona):
    for i in range(len(kontona)):
        print kontona[i]

def degPaBanken(kontona):
    sum = 0
    for i in range(len(kontona)):
        sum += kontona[i].saldo
    return sum

# Huvudprogram
kontona = lasIn()
skrivUt(kontona)
print 'Banken har totalt ', degPaBanken(kontona), ' kr'