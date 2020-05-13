#!/usr/bin/python3

class Rational2(object):

	#-----------------------------------------------
	# constructor
	#-----------------------------------------------
	def __init__( self, newNumerator, newDenominator ):
		self.nominator = newNominator
		self.denominator = newDenominator
		self.simplify()

	#-----------------------------------------------
	# setter / getter
	#-----------------------------------------------

	@property
	def numerator(self):
		return self.__numerator

	@numerator.setter
	def numerator(self, newNumerator):
		if isinstance(newNumerator,int) == False:
			raise BaseExecption( "Numerator must be integer" )
		self.__numerator = newNumerator

	@property
	def denominator(self):
		return self.__denominator

	@denominator.setter
	def denominator(self, newDenominator):
		if isinstance(newDenominator,int) == False:
			raise BaseExecption( "Denominator must be integer" )
		if newDenominator == 0:
			raise BaseExecption( "Denominator cannot be null" )
		self.__denominator = newDenominator

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

