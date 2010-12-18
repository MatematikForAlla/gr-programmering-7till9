#encoding: latin1

class rektangel:
	def __init__(self, h, b):
		self.hojd = h
		self.bredd = b

	def __str__(self):
		return "h=" + str(self.hojd) + " b=" + str(self.bredd)

	def __cmp__(self, rekt):
		a0 = self.hojd * self.bredd
		a1 = rekt.hojd * rekt.bredd
		if a0 < a1:
			return -1
		elif a0 == a1:
			return 0
		return 1

	def skala(self, n):
		self.hojd *= n
		self.bredd *= n

a = rektangel(2,3)
print a
a.skala(3)
print a

