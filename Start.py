#!/usr/bin/python3

from Rational import Rational
from Rational2 import Rational2

# class Ratrional

r1 = Rational( 3, 2 )
r2 = Rational( 4, 8 )

print ( r1 )
print ( r2 )

r1.numerator = 12;
r1.denominator = 24;
print ( r1 )

r1.simplify()
print ( r1 )

# class Ratrional2

r21 = Rational( 3, 2 )
r22 = Rational( 4, 8 )

print ( r21 )
print ( r22 )

r21.numerator = 12;
r21.denominator = 24;
print ( r21 )

r21.simplify()
print ( r21 )
