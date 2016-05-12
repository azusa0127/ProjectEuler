#Problem 53: Combinatoric selections
from math import factorial
import time

def GetCombinations(n,r):
	return (factorial(n)/(factorial(r)*factorial(n-r)))

def CountTermsLargerThan(l):
	count = 0
	for n in range(1,101):
		for r in range(1,n):
			if(GetCombinations(n,r)>l):
				count += 1
	return count
	
print('start')
start = time.time()
print(CountTermsLargerThan(1000000))
print('end')
print(time.time()-start)
