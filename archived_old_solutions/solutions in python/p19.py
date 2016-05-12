##Counting Sundays Problem 19
'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''


def CheckIfLeapYear(year):
	if (year % 4 != 0):
		return False 
	elif (year % 100 == 0):
		if (year % 400 != 0):
			return False
	return True

def GetDaysOfTheMonth(year,month):
	monthWith31Days = [1,3,5,7,8,10,12]
	monthWith30Days = [4,6,9,11]
	if month in monthWith31Days:
		return 31
	elif month in monthWith30Days:
		return 30
	else: 
		if CheckIfLeapYear(year):
			return 29
		else:
			return 28

def CountFirstSundays():
	daySum = 365
	print(daySum%7)
	firstSundayCount = 0
	for yr in range (1901,2001):
		for mn in range(1,13):
			daySum += GetDaysOfTheMonth(yr,mn)
			if (daySum % 7 == 6):
				firstSundayCount += 1
	return firstSundayCount
	
print(CountFirstSundays())
