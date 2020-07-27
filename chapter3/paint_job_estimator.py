"""
- Author: Sharif Ehsani
- Date: June 2020
- www.gitbuh.com/ehsanis

A painting company has determined that for every 115 square feet of wall space, one gallon
of paint and eight hours of labor will be required. The company charges $20.00 per
hour for labor. Write a program that asks the user to enter the square feet of wall space to
be painted and the price of the paint per gallon. The program should display the following
data:
• The number of gallons of paint required
• The hours of labor required
• The cost of the paint
• The labor charges
• The total cost of the paint job
"""

# function to start the program.

def main():
	intro_message()

# function to print intro message to the user
def intro_message():
	print()
	print('This program estimates the total cost of a paint job based on the number of square feet of wall space to be painted.')
	get_input()

# function to get user input
def get_input():
	area_to_paint = float(input('Please enter the wall area to be painted in square feet: '))
	price_of_paint_per_gallon = float(input('Enter the price of paint per gallon: '))
	calculate_total_cost(area_to_paint, price_of_paint_per_gallon)

# function to estimate total cost of the paint job
def calculate_total_cost(area_to_paint, price_of_paint_per_gallon):
	gallon_of_paint = float(area_to_paint / 115)
	hours_of_labor = float((area_to_paint / 115) * 8 )
	cost_of_paint = float(gallon_of_paint * price_of_paint_per_gallon)
	labor_charge = float(hours_of_labor * 20.0)
	total_cost = float(cost_of_paint + labor_charge)
	display_message(gallon_of_paint, hours_of_labor, cost_of_paint, labor_charge, total_cost)

# function to display the product and labour required
def display_message(gallon_of_paint, hours_of_labor, cost_of_paint, labor_charge, total_cost):
	print('The number of gallons of paint required: ', format(gallon_of_paint,'.2f'))
	print('The hours of labour required: ', format(hours_of_labor,'.2f'))
	print('The cost of the paint: ', format(cost_of_paint,'.2f'))
	print('The labour charges "', format(labor_charge,'.2f'))
	print('The total cost of the paint job: ', format(total_cost,'.2f'))
	print()

# call the main function
main()