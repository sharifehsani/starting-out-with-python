
"""
- Author: Sharif Ehsani
- Date: September 2020
- https://github.com/sharifehsani

Programming Exercises 
1. Total Sales
Design a program that asks the user to enter a store’s sales for each day of the week. 
The amounts should be stored in a list. Use a loop to calculate the total sales for the week and display the result.
"""

# main function to start the program
def main():

	# initialize a list variable and assign it to be empty
	sales = []

	# initialize an accumulator
	total = 0.0

	# in a loop that runs 5 times for each day of the week
	for day in range(1, 6):
		print("Enter day", day, "sale amount: ", end='')
		today_sale = float(input())
	
		# populate the list
		sales.append(today_sale)

	# in a loop 
	for sale in sales:
		total += sale

	# print the total sale
	print("The total sale for the week is: ", format(total, '.2f'))


# call the main function
main()

