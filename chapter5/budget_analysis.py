"""
- Author: Sharif Ehsani
- Date: July 2020
- https://github.com/sharifehsani

3. Budget Analysis
Write a program that asks the user to enter the amount that he or she has budgeted for a
month. A loop should then prompt the user to enter each of his or her expenses for the
month, and keep a running total. When the loop finishes, the program should display the
amount that the user is over or under budget.
"""

# main function to start the program
def main():
	print() 		# blanck line to seperate the program from the command line for readablity
	# display intro message about the program
	print("This budgeting program keeps track of your expenses and tells you if you are over or under budget.")
	# call the get_input() function
	get_input()

# function to get user input
def get_input():
	# ask the user the amount s/he has budgeted
	budget_amount = float(input("Enter the amount that you have budgeted: "))

	# keep a condition for the loop
	keep_going = 'y'

	# keep a running tool
	total_expenses = 0.0

	# use a loop to track all expenses of the user
	while (keep_going == 'y'):
		expenses = float(input("Enter each of your expenses for the month: "))
		total_expenses = total_expenses + expenses
		keep_going = input("Do you have more expenses to add? enter 'y' for yes or 'n' for no: ")

	# call the budget_calculator() function and pass budget_amount and total_expenses as parameters
	budget_calculator(budget_amount, total_expenses)

# function to calculate the budget
def budget_calculator(budget_amount, total_expenses):
	over_under = budget_amount - total_expenses
	if (over_under < 0 ):
		# multiply over_under with -1 to get ride of the minues sign in front of over_under
		over = (-1 * over_under)
		print("Oh lala! you have spent $", over, " more than $", budget_amount, " you have budgeted.", sep='')

	elif (over_under == 0):
		print("You have spent exactly the same amount as your budget. Congrates!")
	else:
		print("Wow, I call that 'good job!' you have spent $", over_under, ' from your budget of $', budget_amount, sep='')



# call the main function
main()

