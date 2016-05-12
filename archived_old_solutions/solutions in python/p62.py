'''
Problem 62: Cubic permutations
The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843)
and 66430125 (4053). In fact, 41063625 is the smallest cube which has exactly three
permutations of its digits which are also cube.
Find the smallest cube for which exactly five permutations of its digits are cube.
'''

from collections import Counter,deque
from time import time

cnt = Counter()
cnt['0'] += 1
cubelist = deque()
cubelist.append(0)

def AnalyzeTheCubicOf(n):
	tmp = n**3
	cnt[sorted(str(tmp))] += 1
	cubelist.append(sorted(str(tmp)))

def BuildTheList():
	i = 0
	while max(cnt) < 5:
		i += 1
		AnalyzeTheCubicOf(i)
	return i

def FindTheCubeSet(i):
	for d in cubelist:
		if d == cubelist[i]:
			print(d)

def doProblem():
	FindTheCubeSet(BuildTheList())

start = time()
print('start')
print(doProblem())
end = time()
print('end')
print(end-start)
