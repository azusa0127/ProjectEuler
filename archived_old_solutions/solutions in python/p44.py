#coding: utf-8
'''
Problem 44: Pentagon numbers
Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are: 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not  pentagonal.
Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are
pentagonal and D = |Pk − Pj| is minimised; what is the value of D?
'''
import time

def Pentagon(n):
	return n*(3*n-1)/2

def CheckIfPentagon(x):
	n = ((24*x + 1)**0.5 + 1)/6
	if n == int(n):
		return True
	return False

def doProblem():
	PentaSet = set()
	n = 1
	PentaSet.add(Pentagon(n))
	while True:
		nextPn = Pentagon(n+1)
		for p in PentaSet:
			if (nextPn - p) in PentaSet:
				if CheckIfPentagon(nextPn + p):
					return (nextPn,p,nextPn-p) #(Pk,Pj,D)
		PentaSet.add(nextPn)
		n += 1

print('start')
start = time.time()
print(doProblem())
print('end')
print(time.time()-start)
