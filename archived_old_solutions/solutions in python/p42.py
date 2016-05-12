#coding: utf-8
'''
Problem 42: Coded triangle numbers
The nth term of the sequence of triangle numbers is given by, tn = 1⁄2n(n+1); so the first ten
triangle numbers are:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
By converting each letter in a word to a number corresponding to its alphabetical position
and adding these values we form a word value. For example, the word value for SKY is 19 +
11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a
triangle word.
Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly
two-thousand common English words, how many are triangle words?
'''
import string

def triangleNumSet(limit):
	tnSet = set()
	for n in range(1,limit):
		tnSet.add(n*(n+1)/2)
	return tnSet

def getWordValue(word):
	word = str.lower(word)
	value = 0
	for d in word:
		value += string.ascii_lowercase.index(d) + 1
	return value

def IsTN(s,tSet):
	if getWordValue(s) in tSet:
		return True 
	return False 

def doProblem():
	f = open(Word.txt)
	
