'''
Problem 60: Prime pair sets
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and
concatenating them in any order the result will always be prime. For example, taking 7 and
109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest
sum for a set of four primes with this property.
Find the lowest sum for a set of five primes for which any two primes concatenate to
produce another prime.
'''

from sympy.ntheory import isprime,nextprime, prevprime

dict_primeLinks = {}

def ConcatenatingPrimeTest(a,b):
	if (isprime(int(str(a+b))) and isprime(int(str(b+a)))):
		return True
	return False

dict_primeLinks[3] = set([7,109,673])
dict_primeLinks[7] = set([3,109,673])

print dict_primeLinks

def dictAnalysis(d_primelinks):
	tmpSet = set()
	for kIndex in 
