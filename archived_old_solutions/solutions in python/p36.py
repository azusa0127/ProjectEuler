import numpy
import time

def IfPalindromic(s):
	if s[::-1] == s:
		return True 
	return False

def doProblem():
	sum = 0
	for i in range(1,1000000):
		if IfPalindromic(str(i)):
			if IfPalindromic(numpy.base_repr(i)):
				sum += i
	return sum
		
print('start')
start = time.time()
print(doProblem())
print('end')
print(time.time()-start)
