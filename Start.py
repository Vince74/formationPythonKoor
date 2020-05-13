#!/usr/bin/python3

from Rational import Rational

r = Rational( 3, 2 )
r1 = Rational( 4, 8 )

print ( r )
print ( r1 )

r1.numerator = 4
r1.denominator = 16
r1.simplify()

print ( r1 )

