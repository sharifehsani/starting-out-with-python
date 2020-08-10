"""
- Author: Sharif Ehsani
- Date: July 2020
- www.gitbuh.com/ehsanis

This program calculates a retail item's sale price.
"""

# function to start the program
def main():
	print()

	# sale_price = regular_price - discount
	# discount = regualr_price * discount_percentage

	# call the get_input() function to get regular price and discount percentage
	regular_price, discount_percentage = get_input()

	# call the discount function to calculate the discount 
	discount_amount = discount(regular_price, discount_percentage)

	# call the calculate_sale_price() function and get the sale price
	sale_price = calculate_sale_price(regular_price, discount_amount)

	# display the sale price
	print("The regualr price of the item is: $", format(regular_price, '.2f'), sep='')
	print("You save : $", format(discount_amount, '.2f'), sep='')
	print("The sale price after the discount is : $", format(sale_price, '.2f'), sep='')




# function to get user input
def get_input():
	regular_price = float(input("Enter item's regualr price: "))
	discount_percentage = float(input("Enter the discount_percentage: "))
	return regular_price, discount_percentage


# funciton to calculate the discount amount
def discount(regular_price, discount_percentage):
	return (regular_price * (discount_percentage / 100))


# function to calculate the sale price of the item
def calculate_sale_price(regular_price, discount_amount):
	regular_price = regular_price - discount_amount
	return regular_price


# call the main function
main()