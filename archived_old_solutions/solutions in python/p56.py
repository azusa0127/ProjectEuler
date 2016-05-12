#Problem 56: Powerful digit sum
import time

def SumDigits(n):
	sum = 0
	if(n>=10):
		sum = SumDigits(n//10)
	sum += (n%10)
	return sum

def FindMaxSum():
	max = 0
	for i in range(75,100):
		for j in range(90,100):
			if(SumDigits(i**j) > max):
				max = SumDigits(i**j)
	return max

print('start')
start = time.time()
print(FindMaxSum())
print('end')
print(time.time()-start)
