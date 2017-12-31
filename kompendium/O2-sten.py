def rektangel(rad, kol):
    for i in range(rad):
        s = ''
        for j in range(kol):
            s = s +'*'
        print s

rektangel(2,3)

def palindrom(s):
    langd = len(s)
    p = True
    for i in range(langd/2):
        if s[i] != s[langd-i-1]:
            p = False
    return p


ord = 'Vadsomhelst'
while ord != '':
    ord = raw_input('Ange ett ord: ');
    if palindrom(ord):
        print ord + ' är ett palindrom'
    else:
        print ord + ' är ej ett palindrom'
