"""
- Author: Sharif Ehsani
- Date: June 2020
- www.gitbuh.com/ehsanis

10. Monthly Sales Tax
A retail company must file a monthly sales tax report listing the total sales for the month,
and the amount of state and county sales tax collected. The state sales tax rate is 4 percent
and the county sales tax rate is 2 percent. Write a program that asks the user to enter the
total sales for the month. From this figure, the application should calculate and display the
following:
• The amount of county sales tax
• The amount of state sales tax
• The total sales tax (county plus state)
"""

# function to start the program
def main():
	intro_message()


# function to display intro messages
def intro_message():
	print()
	print("This program calculates and display the amount of federal tax and provincial tax on a company's monthly sale")
	get_input()

# function to get user input
def get_input():
	total_sale = float(input("Please enter the total sales for the month: "))
	calculate_tax(total_sale)

# function to calcualte taxes
def calculate_tax(total_sale):
	pst = total_sale * 0.02				# pst = provincial sales tax
	gst = total_sale * 0.04				# gst = government sales tax
	total_sales_tax = pst + gst
	display_message(pst, gst, total_sales_tax)

# function to display message
def display_message(pst, gst, total_sales_tax):
	print('The amount of provintial tax = $', format(pst, '.2f'))
	print('The amount of federal tax = $', format(gst, '.2f'))
	print('The total sales tax (federal plus provincial) = $', format(total_sales_tax, '.2f'))
	print()


# call the main function

main()