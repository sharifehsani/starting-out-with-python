"""
- Author: Sharif Ehsani
- Date: October 2020
- www.gitbuh.com/ehsanis

3. Date Printer
Write a program that reads a string from the user containing a date in the form
mm/dd/yyyy. It should print the date in the form March 12, 2012.

"""

# main function to start the program
def main():

	# get user input
	my_date = input("Please enter the date in this format, mm/dd/yyyy: ")

	# initialize variable to hold the index position of the string when string is sliced
	month = my_date[0:2]
	day = my_date[3:5]
	year = my_date[6:]

	# check all possible options from the 12 months
	month_in_word = ''
	if (month == '01'):
		month_in_word = "January"
	elif (month == '02'):
		month_in_word = "February"
	elif (month == '03'):
		month_in_word = "March"
	elif (month == '04'):
		month_in_word = "April"
	elif (month == '05'):
		month_in_word = "May"
	elif (month == '06'):
		month_in_word = "June"
	elif (month == '07'):
		month_in_word = "July"
	elif (month == '08'):
		month_in_word = "August"
	elif (month == '09'):
		month_in_word = "September"
	elif (month == '10'):
		month_in_word = "October"
	elif (month == '11'):
		month_in_word = "November"
	elif (month == '12'):
		month_in_word = "December"

	print(month_in_word," ", day, ", ", year,".", sep='')


# call the main function
main()