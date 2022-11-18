"""
- Author: Sharif Ehsani
- Date: June 2020
- https://github.com/sharifehsani

6. Change for a Dollar Game
Create a change-counting game that gets the user to enter the number of coins required to make
exactly one dollar. The program should prompt the user to enter the number of pennies,
nickels, dimes, and quarters. If the total value of the coins entered is equal to one dollar, the program
should congratulate the user for winning the game. Otherwise, the program should display
a message indicating whether the amount entered was more than or less than one dollar.
"""
PENNY = 1
NICKEL = 5
DIME = 10
QUARTER = 25

# main function to start the program
def main():
	print()
	print("This change for a dollar game requires user to enter exact amount of coins pennies, dimes, nickels and quarter to win a dollar. ")
	get_input()

# function to get user input
def get_input():
	pennies = int(input("Enter the number of pennies: "))
	nickels = int(input("Enter the number of nickels: "))
	dimes = int(input("Enter the number of dimes: "))
	quarters = int(input("Enter the number of quarters: "))
	calculate_dollar(pennies, nickels, dimes, quarters)

# function to calculate dollar
def calculate_dollar(pennies, nickels, dimes, quarters):
	pennies_total = PENNY * pennies
	nickels_total = NICKEL * nickels
	dimes_total = DIME * dimes
	quarters_toal = QUARTER * quarters
	subtotal = pennies_total + nickels_total + dimes_total + quarters_toal

	if (subtotal == 100):
		print("Horray! congratulations! you won one dollar.")
	elif (subtotal > 100):
		print('The amount entered "', subtotal, '" was greater than a dollar.')
	else:
		print('The amount entered "', subtotal, '" was less than a dollar.')

# call the main function
main()
	
