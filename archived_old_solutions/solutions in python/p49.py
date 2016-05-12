'''
Problem 49: Prime permutations
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
What 12-digit number do you form by concatenating the three terms in this sequence?
'''
import time
from sympy import isprime
from itertools import permutations

def GetArithmeticPerms(tuple_n):
	subPerms = list(map("".join, permutations(tuple_n)))
	arithmaticPerms = []
	if '1487' in subPerms:
		return arithmaticPerms
	for j in subPerms[1:-1]:
		for i in subPerms[:-1]:
			if int(i) >= int(j):
				break 
			k = str(int(j)*2 - int(i))
			if k in subPerms:
				arithmaticPerms.append((i,j,k))
	return arithmaticPerms

def PrimeTestForTuple(t):
	for e in t:
		if isprime(int(e))== False:
			return False
	return True

def CheckPrimeInArithPermList(list_arthPerm):
	for t in list_arthPerm:
		if PrimeTestForTuple(t):
			return t
	return False

def doProblem():
	soln = set()
	for i in range(1488,9998):
		tmp = CheckPrimeInArithPermList(GetArithmeticPerms(tuple(str(i)))) 
		if tmp != False:
			print("".join(tmp))
			return tmp

print('start')
start = time.time()
print(doProblem())
print('end')
print(time.time()-start)
