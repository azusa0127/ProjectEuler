'''
Digit canceling fractions
Problem 33
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''
from sets import Set
from fractions import Fraction

def CheckFrac(i,n,d):
	if float(n+i)/float(i+d) == float(n)/float(d):
		return True
	return False 

def solution():
	solSet = set()
	for i in range(1,10):
		rangeSet = Set(['1','2','3','4','5','6','7','8','9'])
		rangeSet.remove(str(i))
		for n in rangeSet:
			for d in rangeSet:
				if CheckFrac(str(i),n,d):
					solSet.add(n+str(i)+'/'+str(i)+d)
	return solSet

def ToFracSet(_set):
	newSet = set()
	for i in _set:
		newSet.add(Fraction(i))
	return newSet

def ProductOfFracSet(fracSet):
	product = 1
	for frac in fracSet:
		product *= frac
	return product
	
print(ProductOfFracSet(ToFracSet(solution())))
					
					
