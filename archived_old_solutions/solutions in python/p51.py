'''
Problem 51: Prime digit replacements
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible
values: 13, 23, 43, 53, 73, and 83, are all prime.
By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the
first example having seven primes among the ten generated numbers, yielding the family:
56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first
member of this family, is the smallest prime with this property.
Find the smallest prime which, by replacing part of the number (not necessarily adjacent
digits) with the same digit, is part of an eight prime value family.
'''

from sympy import primerange

def GetSetOfPrimesInRange(e):
	primeSet = set()
	for p in primerange(10**e,10**(e+1)):
		if (str(p)[-1] in ('1','3','7')):
			primeSet.add(p)
	return primeSet

def DigitCompare(number1,number2,digitIndex):
	if (str(number1)[digitIndex] == str(number2)[digitIndex]):
		return True
	return False
	
print(GetSetOfPrimesInRange(1))
