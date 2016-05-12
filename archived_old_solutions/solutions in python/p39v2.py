#coding: utf-8
'''
Integer right triangles
Problem 39
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''
import time
from collections import Counter

def doProblem():
	sol = Counter()
	ROOT2OVER2 = (2**0.5)/2
	for c in range(3,500):
		for a in range(1,int(c*ROOT2OVER2)+1):
			b = (c*c - a*a)**0.5
			if b - int(b) == 0:
				p = a + int(b) + c
				sol[p] += 1	
	return sol.most_common(1)

print('start')
start = time.time()
print(doProblem())
print('end')
print(time.time()-start)
