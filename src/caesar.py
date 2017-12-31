#encoding: iso-8859-1

alfabet = "abcdefghijklmnopqrstuvwxyzåäö"

##########################
# Funktioner
##########################

# funktion för att kryptera med caesarskiffer
def kryptera(text, nyckel):
	# hitta nyckelbokstavens index, ex sjätte bokstaven.
	index = alfabet.index(nyckel)
	# bygg ett kryptoalfabet (gör en förskjutning)
	kryptoalfabet = alfabet[index:]
	kryptoalfabet = kryptoalfabet + alfabet[:index]
	kryptoalfabet = kryptoalfabet.upper()
	# här sparar vi det krypterade meddelandet
	kryptotext = ""
	
	# för varje bokstav i texten
	for bokstav in text:
		# hitta bokstavens index
		index = alfabet.index(bokstav)
		# översätt bokstaven
		kryptotext = kryptotext + kryptoalfabet[index]

	# skicka tillbaka den färdiga texten
	return kryptotext


# funktion för att avkryptera med caesarskiffer
def avkryptera(kryptotext, nyckel):
	# hitta nyckelbokstavens index, ex sjätte bokstaven.
	index = alfabet.index(nyckel)
	# bygg ett kryptoalfabet (gör en förskjutning)
	kryptoalfabet = alfabet[index:]
	kryptoalfabet = kryptoalfabet + alfabet[:index]
	kryptoalfabet = kryptoalfabet.upper()
	# här sparar vi de avkrypterade meddelandet
	text = ""
	
	# för varje bokstav i texten
	for bokstav in kryptotext:
		# hitta bokstavens index
		index = kryptoalfabet.index(bokstav)
		# översätt bokstaven
		text = text + alfabet[index]

	# skicka tillbaka den färdiga texten
	return text


# funktion för att knäcka ett caesarskiffer
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

# läs in ett val från tangentbordet
val = raw_input("Vad vill du göra? (kryptera, avkryptera, bruteforce) ")
if val == "kryptera":
	nyckel = raw_input("Ange nyckel (liten bokstav):")
	text = raw_input("Text att kryptera:")
	print kryptera(text, nyckel)
elif val == "avkryptera":
	nyckel = raw_input("Ange nyckel (liten bokstav):")
	text = raw_input("Text att avkryptera:")
	print avkryptera(text, nyckel)
elif val == "bruteforce":
	text = raw_input("Text att knäcka:")
	print bruteforce(text)
else:
	print "Tyvärr förstod jag inte:", val

raw_input("Tryck en tangent för avslut ...")
