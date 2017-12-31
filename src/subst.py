#encoding: iso-8859-1

alfabet = "abcdefghijklmnopqrstuvwxyz���"

##########################
# Funktioner
##########################

# funktion f�r att kryptera med substitutionsskiffer
# alfabet: a b c d e f g h ...
# nyckel:  X Q C D B L M O ...
# adabada -> XDXQXDX
def kryptera(text, nyckel):
	nyckel = nyckel.upper() # nyckeln ska ha stora bokst�ver
	text = text.lower() # texten ska ha bara sm� bokst�ver
	# h�r sparar vi det krypterade meddelandet
	kryptotext = ""

	# f�r varje bokstav i texten
	for bokstav in text:
		# hitta bokstavens index
		index = alfabet.index(bokstav)
		# �vers�tt bokstaven
		kryptotext = kryptotext + nyckel[index]

	# skicka tillbaka den f�rdiga texten
	return kryptotext


# funktion f�r att avkryptera med substitutionsskiffer
# alfabet: a b c d e f g h ...
# nyckel:  X Q C D B L M O ...
# XDXQXDX -> adabada
def avkryptera(kryptotext, nyckel):
	nyckel = nyckel.upper() # nyckeln ska ha bara stora bokst�ver
	kryptotext = kryptotext.upper() # kryptotexten ska ocks� ha stora bokst�ver
	# h�r sparar vi det avkrypterade meddelandet
	text = ""
	
	# f�r varje bokstav i texten
	for bokstav in kryptotext:
		# hitta bokstavens index
		index = nyckel.index(bokstav)
		# �vers�tt bokstaven
		text = text + alfabet[index]

	# skicka tillbaka den f�rdiga texten
	return text


##########################
# Huvudprogram
##########################

print "David Erik Filip Kryptoapparat"

# l�s in ett val fr�n tangentbordet
val = raw_input("Vad vill du g�ra? (kryptera, avkryptera) ")
if val == "kryptera":
	nyckel = raw_input("Ange nyckel (ett alfabete i oordning):")
	text = raw_input("Text att kryptera:")
	print kryptera(text, nyckel)
elif val == "avkryptera":
	nyckel = raw_input("Ange nyckel (som anv�ndes f�r krypteringen):")
	text = raw_input("Text att avkryptera:")
	print avkryptera(text, nyckel)
else:
	print "Tyv�rr f�rstod jag inte:", val

raw_input("Tryck en tangent f�r avslut ...")
