#coding: utf-8
'''
Integer right triangles
Problem 39
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''
import time

def CheckIfRightTri(a,b,c):
	if a*a == b*b + c*c :
		return True 
	return False 

def doProblem():
	maxIndex = 0
	maxCount = 0
	for p in range(4,1001):
		count = 0
		aRange = range(p//3,p-2)
		for a in aRange:
			bRange = range(1,(p-a)//2)
			for b in bRange:
				c = p - a - b
				if CheckIfRightTri(a,b,c):
					count += 1
		if count > maxCount:
			maxCount = count
			maxIndex = p
	return (maxIndex,maxCount)

print('start')
start = time.time()
print(doProblem())
print('end')
print(time.time()-start)
				
