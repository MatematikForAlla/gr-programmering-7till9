#encoding: latin1
# tar upp bregreppen:
## typkonvertering
## funktion (med returv�rde)
## aritmetiska operatorer
## j�mf�relseoperatorer
## logiska operatorer
## while-slinga
## for-slinga
## range()
## if-elif-else-sats

# weight �r vikten, i gram, hos ett brev.
# r�tt porto returneras.
def check_postage(weight):
    ## POSTENS 1:a KLASS INRIKES BREV
    if (weight <= 20):
        return 6
    elif (weight <= 100):
        return 12
    elif (weight <= 250):
        return 24
    elif (weight <= 500):
        return 36
    elif (weight <= 1000):
        return 48
    elif (weight <= 2000):
        return 72
    ## POSTENS POSTPAKET
    elif (weight <= 3000):
        return 150
    elif (weight <= 5000):
        return 175
    elif (weight <= 10000):
        return 225
    elif (weight <= 15000):
        return 275
    elif (weight <= 20000):
        return 320
    return -1


#####################
# Huvudprogrammet
#####################

# Loopa s� l�nge som m�jligt
while (True):
    print "V�lkommen till Brevv�gen"
    nletters = raw_input("Hur m�nga brev vill du ber�kna porto f�r (0 " \
        "f�r att avsluta): ")
    nletters = int(nletters)
    # 0 f�r att avsluta (negativa ocks�)
    if (nletters <= 0):
        break
    sum = 0
    for i in range(nletters):
        w = raw_input("Hur mycket v�ger brev " + str(i+1) + ": ")
        postage = check_postage(float(w))
        if (postage < 0):
            print "Den vikten finns inte med i portotabellen."
        else:
            print "Du m�ste betala", postage, "SEK i porto."
            sum += postage
    if (nletters > 1):
        print "Det blir", sum, "SEK f�r alla brev, tack!"
    elif (sum > 100 and nletters == 1):
        print "Mycket pengar f�r ett postpaket!"

raw_input("Tryck en tangent f�r avslut ...")
