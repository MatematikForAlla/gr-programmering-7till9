#encoding: iso-8859-1

alfabet = "abcdefghijklmnopqrstuvwxyzåäö"

##########################
# Funktioner
##########################

# funktion för att kryptera med substitutionsskiffer
# alfabet: a b c d e f g h ...
# nyckel:  X Q C D B L M O ...
# adabada -> XDXQXDX
def kryptera(text, nyckel):
	nyckel = nyckel.upper() # nyckeln ska ha stora bokstäver
	text = text.lower() # texten ska ha bara små bokstäver
	# här sparar vi det krypterade meddelandet
	kryptotext = ""

	# för varje bokstav i texten
	for bokstav in text:
		# hitta bokstavens index
		index = alfabet.index(bokstav)
		# översätt bokstaven
		kryptotext = kryptotext + nyckel[index]

	# skicka tillbaka den färdiga texten
	return kryptotext


# funktion för att avkryptera med substitutionsskiffer
# alfabet: a b c d e f g h ...
# nyckel:  X Q C D B L M O ...
# XDXQXDX -> adabada
def avkryptera(kryptotext, nyckel):
	nyckel = nyckel.upper() # nyckeln ska ha bara stora bokstäver
	kryptotext = kryptotext.upper() # kryptotexten ska också ha stora bokstäver
	# här sparar vi det avkrypterade meddelandet
	text = ""
	
	# för varje bokstav i texten
	for bokstav in kryptotext:
		# hitta bokstavens index
		index = nyckel.index(bokstav)
		# översätt bokstaven
		text = text + alfabet[index]

	# skicka tillbaka den färdiga texten
	return text


##########################
# Huvudprogram
##########################

print "David Erik Filip Kryptoapparat"

# läs in ett val från tangentbordet
val = raw_input("Vad vill du göra? (kryptera, avkryptera) ")
if val == "kryptera":
	nyckel = raw_input("Ange nyckel (ett alfabete i oordning):")
	text = raw_input("Text att kryptera:")
	print kryptera(text, nyckel)
elif val == "avkryptera":
	nyckel = raw_input("Ange nyckel (som användes för krypteringen):")
	text = raw_input("Text att avkryptera:")
	print avkryptera(text, nyckel)
else:
	print "Tyvärr förstod jag inte:", val

raw_input("Tryck en tangent för avslut ...")
