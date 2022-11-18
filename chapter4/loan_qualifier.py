""""
- Author: Sharif Ehsani
- Date: June 2020
- https://github.com/sharifehsani

This program determines if a customer qualifies for credit card
MIN_SALARY = 30,000
MIN_YEAR_JOB = 2
"""

# function start the program
def main():
	print("This program determines if a customer qualifies for credit card.")
	get_input()

# funtion to get user input
def get_input():
	salary = float(input("Enter your annual income: "))
	year_on_job = float(input("Enter number of years employed: "))
	determine_qualification(salary, year_on_job)

# function to determine qualification
def determine_qualification(salary, year_on_job):
	if (salary >= 30000):
		if (year_on_job >= 2):
			print("You are approved for the loan!.")
		else:
			print("Sorry, you are not approved for the loan, minimum required years employed is 2 years.")
	else:
		print("Sorry, you are not approved for the loan, the minimum required annual salary is $30,000 ")


main()
