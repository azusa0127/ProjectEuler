#coding: utf-8
'''
Problem 40: Champernowne's constantAn irrational decimal fraction is created by concatenating the positive integers:0.123456789101112131415161718192021...It can be seen that the 12th digit of the fractional part is 1.If dn represents the nth digit of the fractional part, find the value of the followingexpression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
'''
import time

def doProblem():
	soln = 1
	df = 1
	count = 0
	currentIndex = 0
	i = 0
	while count < 7:
		while currentIndex < df:
			i += 1
			currentIndex += len(str(i))
		soln *= int(str(i)[-(currentIndex+1-df)])
		df *= 10
		count += 1
	
	return soln

print('start')
start = time.time()
print(doProblem())
print('end')
print(time.time()-start)
