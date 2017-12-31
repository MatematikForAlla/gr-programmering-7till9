#encoding: latin1

alfabet = "abcdefghijklmnopqrstuvwxyz���"

##########################
# Funktioner
##########################

def rakna(text):
	antal = [0]*len(alfabet)
	for bokstav in text:
		try:
			index = alfabet.index(bokstav)
		except:
			# om bokstaven inte finns med i alfabetet hamnar vi h�r.
			# t.ex. finns inte tecknet f�r mellanslag, punkt eller komma med.
			pass
		else:
			# annars r�knar vi tecknet
			antal[index] = antal[index] + 1
	total = 0
	for i in range(len(antal)):
		total = total + antal[i]
	for i in range(len(antal)):
		antal[i] = float(antal[i])/total
	return antal


##########################
# Huvudprogram
##########################

text = raw_input("Ange text f�r frekvensanalys: ")
frekvens = rakna(text)

for i in range(len(alfabet)):
	print "P(", alfabet[i], ") = ", frekvens[i]

raw_input("Tryck enter f�r avslut ...")
