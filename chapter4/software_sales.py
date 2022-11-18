"""
- Author: Sharif Ehsani
- Date: June 2020
- https://github.com/sharifehsani

8. Software Sales
A software company sells a package that retails for $99. Quantity discounts are given
according to the following table:
Quantity Discount
10–19 20%
20–49 30%
50–99 40%
100 or more 50%
Write a program that asks the user to enter the number of packages purchased. The program
should then display the amount of the discount (if any) and the total amount of the
purchase after the discount.
"""

PACKAGE_PRICE = 99
DISCOUNT = 0.0

# main function to start the program
def main():
	print()
	print("This program calculates a software company's sales and discounts.")
	get_input()

# function to get user input
def get_input():
	number_of_packages = int(input("Enter the number of packages purchased: "))
	calculate_discount(number_of_packages)

# function to calculate discount
def calculate_discount(number_of_packages):
	if (number_of_packages < 10):
		DISCOUNT = 0.0
		total_before_discount = number_of_packages * 99
		discount_amount = total_before_discount * DISCOUNT
		total_after_discount = total_before_discount - discount_amount

	elif (number_of_packages >= 10 and number_of_packages <= 19):
		DISCOUNT = 0.20
		total_before_discount = number_of_packages * 99
		discount_amount = total_before_discount * DISCOUNT
		total_after_discount = total_before_discount - discount_amount

	elif (number_of_packages >= 20 and number_of_packages <= 49):
		DISCOUNT = 0.30
		total_before_discount = number_of_packages * 99
		discount_amount = total_before_discount * DISCOUNT
		total_after_discount = total_before_discount - discount_amount

	elif (number_of_packages >= 50 and number_of_packages <= 99):
		DISCOUNT = 0.40
		total_before_discount = number_of_packages * 99
		discount_amount = total_before_discount * DISCOUNT
		total_after_discount = total_before_discount - discount_amount

	else:
		DISCOUNT = 0.50
		total_before_discount = number_of_packages * 99
		discount_amount = total_before_discount * DISCOUNT
		total_after_discount = total_before_discount - discount_amount

	# call display_message function	
	display_message(total_before_discount, discount_amount, total_after_discount)

# function to display message
def display_message(total_before_discount,discount_amount, total_after_discount):
	print("Total amount before discount: $", format(total_before_discount, '.2f'), sep='')
	print("The discount amount: $", format(discount_amount, '.2f'), sep='')
	print('Total amount after discount: $', format(total_after_discount, '.2f'), sep='')

# call the main function
main()
