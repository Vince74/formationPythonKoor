#!/usr/bin/python3

class Rational(object):

	def __init__( self, num, den ):
		if den == 0:
			raise BaseExecption( "Denominator cannot be null" )
		self.numerator = num
		self.denominator = den

	def __str__( self ):
		return "[%d/%d]" % ( self.numerator, self.denominator )
