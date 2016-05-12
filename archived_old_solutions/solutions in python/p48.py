'''
Problem 48: Self powers
The series, 11 + 22 + 33 + ... + 1010 = 10405071317.
Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
'''
import time

def FindTheSum(l):
	sum = 0
	for i in range(1,l+1):
		sum += i**i
	return sum

def GetLastTenDigis(n):
	return str(n)[-10:]
	
print('start')
start = time.time()
print(GetLastTenDigis(FindTheSum(1000)))
print(time.time()-start)
