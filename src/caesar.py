#encoding: iso-8859-1

alfabet = "abcdefghijklmnopqrstuvwxyz���"

##########################
# Funktioner
##########################

# funktion f�r att kryptera med caesarskiffer
def kryptera(text, nyckel):
	# hitta nyckelbokstavens index, ex sj�tte bokstaven.
	index = alfabet.index(nyckel)
	# bygg ett kryptoalfabet (g�r en f�rskjutning)
	kryptoalfabet = alfabet[index:]
	kryptoalfabet = kryptoalfabet + alfabet[:index]
	kryptoalfabet = kryptoalfabet.upper()
	# h�r sparar vi det krypterade meddelandet
	kryptotext = ""
	
	# f�r varje bokstav i texten
	for bokstav in text:
		# hitta bokstavens index
		index = alfabet.index(bokstav)
		# �vers�tt bokstaven
		kryptotext = kryptotext + kryptoalfabet[index]

	# skicka tillbaka den f�rdiga texten
	return kryptotext


# funktion f�r att avkryptera med caesarskiffer
def avkryptera(kryptotext, nyckel):
	# hitta nyckelbokstavens index, ex sj�tte bokstaven.
	index = alfabet.index(nyckel)
	# bygg ett kryptoalfabet (g�r en f�rskjutning)
	kryptoalfabet = alfabet[index:]
	kryptoalfabet = kryptoalfabet + alfabet[:index]
	kryptoalfabet = kryptoalfabet.upper()
	# h�r sparar vi de avkrypterade meddelandet
	text = ""
	
	# f�r varje bokstav i texten
	for bokstav in kryptotext:
		# hitta bokstavens index
		index = kryptoalfabet.index(bokstav)
		# �vers�tt bokstaven
		text = text + alfabet[index]

	# skicka tillbaka den f�rdiga texten
	return text


# funktion f�r att kn�cka ett caesarskiffer
def bruteforce(text):
	alla = ""
	# varje bokstav i alfabetet kan vara en nyckel
	for bokstav in alfabet:
		# testa att avkryptera och klipp ihop resultaten
		alla = alla + avkryptera(text, bokstav) + ","
	# returnera alla avkrypteringar
	return alla


##########################
# Huvudprogram
##########################

print "Adam Bertil Caesar Kryptoapparat"

# l�s in ett val fr�n tangentbordet
val = raw_input("Vad vill du g�ra? (kryptera, avkryptera, bruteforce) ")
if val == "kryptera":
	nyckel = raw_input("Ange nyckel (liten bokstav):")
	text = raw_input("Text att kryptera:")
	print kryptera(text, nyckel)
elif val == "avkryptera":
	nyckel = raw_input("Ange nyckel (liten bokstav):")
	text = raw_input("Text att avkryptera:")
	print avkryptera(text, nyckel)
elif val == "bruteforce":
	text = raw_input("Text att kn�cka:")
	print bruteforce(text)
else:
	print "Tyv�rr f�rstod jag inte:", val

raw_input("Tryck en tangent f�r avslut ...")
