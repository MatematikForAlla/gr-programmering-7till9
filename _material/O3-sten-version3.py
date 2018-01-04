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
    infil.close()
    return kontona

def sparaPaFil(kontona):
    utfil = open('utfil.txt','w')
    for i in range(len(kontona)):
        utfil.write(str(kontona[i].nr) + '/' + kontona[i].namn +'/' + str(kontona[i].saldo)+ '\n')
    utfil.close()
    

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

val = ''
while val != '0':
    print '0 - avsluta'
    print '1 - skriv ut alla konton'
    print '2 - skriv ut summan av insatta pengar'
    print '3 - sätt in 50kr åt alla!'
    val = raw_input('Ditt val: ')
    if val == '1':
        skrivUt(kontona)
    elif val == '2':
        print 'Banken har totalt ', degPaBanken(kontona), ' kr'
    elif val == '3':
        for k in kontona:
            k.deposit(50)


sparaPaFil(kontona)
