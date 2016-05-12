'''
Consecutive prime sum
Problem 50
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''
from time import time
from sympy.ntheory import isprime, nextprime, prevprime

def GetLongestConsSumPrimes(step,limit):
	sum = step
	count = 1
	i = nextprime(step)
	while (sum + i)<limit:
		sum += i
		count += 1
		i = nextprime(i)
		
	while isprime(sum) == False :	
		i = prevprime(i)
		sum -= i
		count -= 1

	return (count,sum)

def doProblem():
	LIMIT = 1000000
	step = 2
	maxLength = 0
	maxIndex = 0
	maxSum = 0
	while step < (LIMIT-maxSum):
		if GetLongestConsSumPrimes(step,LIMIT)[0] > maxLength:
			maxLength = GetLongestConsSumPrimes(step,LIMIT)[0]
			maxSum = GetLongestConsSumPrimes(step,LIMIT)[1]
			maxIndex = step
			print(maxIndex,maxLength,maxSum)
		step = nextprime(step)
	return (maxIndex,maxLength,maxSum)
	
start = time()
print('start')
print(doProblem())
end = time()
print('end')
print(end-start)
