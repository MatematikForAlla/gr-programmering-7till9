#encoding: latin1

class Fraction:
	def __init__(self, nom, den=1):
		self.__nom = nom
		self.__den = den

	def __str__(self):
		return str(self.__nom)+"/"+str(self.__den)

	def __add__(self, frac):
		nom = self.__nom * frac.__den
		nom += frac.__nom * self.__den
		den = self.__den * frac.__den
		return Fraction(nom, den)

	def __mul__(self, frac):
		nom = self.__nom * frac.__nom
		den = self.__den * frac.__den
		return Fraction(nom, den)

	def __cmp__(self, frac):
		nom0 = self.__nom * frac.__den
		nom1 = frac.__nom * self.__den
		if nom0 < nom1:
			return -1
		elif nom0 > nom1:
			return 1
		return 0


f0 = Fraction(1,3)
f1 = Fraction(2,3)
f2 = Fraction(1,4)

print f1, "+", f0, "=", f1+f0
print f1, "*", f2, "=", f1*f2

