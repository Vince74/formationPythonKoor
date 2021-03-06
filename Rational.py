#!/usr/bin/python3

class Rational(object):

	#-----------------------------------------------
	# constructor
	#-----------------------------------------------
	def __init__( self, newNumerator, newDenominator ):
		self.__setNumerator(newNumerator);
		self.__setDenominator(newDenominator);
		self.simplify()

	#-----------------------------------------------
	# setter / getter
	#-----------------------------------------------
	def __getNumerator(self):
		return self.__numerator

	def __setNumerator(self, newNumerator):
		if isinstance(newNumerator,int) == False:
			raise BaseExecption( "Numerator must be integer" )
		self.__numerator = newNumerator

	def __getDenominator(self):
		return self.__denominator

	def __setDenominator(self, newDenominator):
		if isinstance(newDenominator,int) == False:
			raise BaseExecption( "Denominator must be integer" )
		if newDenominator == 0:
			raise BaseExecption( "Denominator cannot be null" )
		self.__denominator = newDenominator

	#---------------------------------------------------------------------
	# Property: paire de methodes (getter + setter) d'acces a un attribut
	#---------------------------------------------------------------------
	numerator = property( __getNumerator, __setNumerator )
	denominator = property( __getDenominator, __setDenominator )

	#-----------------------------------------------
	# methods
	#-----------------------------------------------
	def simplify(self):
		divisor = 2
		# recherche du plus petit diviseur commun
		while divisor <= min(self.__numerator, self.__denominator):
			while self.__numerator % divisor == 0 and self.__denominator % divisor == 0:
				self.__numerator /= divisor
				self.__denominator /= divisor
			divisor += 1

	def __str__( self ):
		return "[%d/%d]" % ( self.__numerator, self.__denominator )

