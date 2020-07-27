"""
- Author: Sharif Ehsani
- Date: June 2020
- www.gitbuh.com/ehsanis

4. Magic Dates
The date June 10, 1960, is special because when it is written in the following format, the
month times the day equals the year:
6/10/60
Design a program that asks the user to enter a month (in numeric form), a day, and a twodigit
year. The program should then determine whether the month times the day equals the
year. If so, it should display a message saying the date is magic. Otherwise, it should display
a message saying the date is not magic.
"""

# function to start the program
def main():
	print()
	print("This program calculates magic dates by finding if the day times month equals last two digits of the year.")
	get_input()

# function to get input
def get_input():
	month = int(input('Enter the month of the year in numeric form. For example "January = 1" and "December = 12": '))
	day = int(input("Enter the day of the year in numeric form: "))
	year = int(input("Enter the last 2 digits of the year in numeric form. For example , Enter 60 for 1960: "))
	calculate_magic_date(month, day, year)

# function to calculate magic date
def calculate_magic_date(month, day, year):
	magic_date = month * day
	if (magic_date == year):
		print("Wow! The date is magic!", month, " * ", day, " = ", year)
	else:
		print("The date is not magic.", month, " * ", day, " != ", year)

#call the main function
main()