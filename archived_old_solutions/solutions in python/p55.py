#Problem 55: Lychrel number
import time

def ReverseNum(n):
	new = 0
	while (n>0):
		new = new * 10 + n%10
		n = n//10
	return new

def CheckIfPal(n):
	if (n ==ReverseNum(n)):
		return True
	else:
		return False

def CheckIfLychrel(n):
	count = 0
	while (count<50):
		count += 1
		n += ReverseNum(n)
		if CheckIfPal(n):
			return False
	return True 

def CountAllLychrelNums(limit):
	count = 0
	for i in range(1,limit):
		if (CheckIfLychrel(i)):
			count += 1
	return count

print('start')
start = time.time()
print(CountAllLychrelNums(10000))
print('end')
print(time.time()-start)
