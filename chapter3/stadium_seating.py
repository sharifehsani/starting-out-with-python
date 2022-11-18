"""
- Author: Sharif Ehsani
- Date: June 2020
- https://github.com/sharifehsani

8. Stadium Seating
There are three seating categories at a stadium. For a softball game, Class A seats cost $15,
Class B seats cost $12, and Class C seats cost $9. Write a program that asks how many tickets
for each class of seats were sold, and then displays the amount of income generated from
ticket sales.
"""

# main function to start the program
def main():
	intro_message() # call the infro_message function

# function to print intro message
def intro_message():
	print('This program calculates the income generated from ticket sales of the softball game.')
	print('There are three seating categories: class A, class B, class C')
	get_input()

# function to get user input
def get_input():
	class_a = float(input('Please enter the number of tickets sold from class A: '))
	class_b = float(input('Please enter the number of tickets sold from class B: '))
	class_c = float(input('Please enter the number of tickets sold from class C: '))
	calculate_income(class_a, class_b, class_c)

# function to calculate income generated from the ticket sale
def calculate_income(sale_a,sale_b,sale_c):
	price_of_seat_in_class_a = 15
	price_of_seat_in_class_b = 12
	price_of_seat_in_class_c = 9
	total_income = (sale_a * price_of_seat_in_class_a) + (sale_b * price_of_seat_in_class_b) + (sale_c * price_of_seat_in_class_c)
	print('The total amount of income generated from ticket sales is = $', format(total_income, '.2f'))

# call the main function
main()
