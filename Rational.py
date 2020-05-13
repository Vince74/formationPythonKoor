#!/usr/bin/python3

class Rational(object):

	def __init__( self, num, den ):
		if den == 0:
			raise BaseExecption( "Denominator cannot be null" )
		self.numerator = num
		self.denominator = den
		self.simplify()

	def __str__( self ):
		return "[%d/%d]" % ( self.numerator, self.denominator )

	def simplify(self):
		divisor = 2
		# recherche du plus petit diviseur commun
		while divisor <= min(self.numerator, self.denominator):
			while self.numerator % divisor == 0 and self.denominator % divisor == 0:
				self.numerator /= divisor
				self.denominator /= divisor
			divisor += 1
			
