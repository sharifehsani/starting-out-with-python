"""
- Author: Sharif Ehsani
- Date: July 2020
- www.gitbuh.com/ehsanis

10. Future Value
Suppose you have a certain amount of money in a savings account that earns compound
monthly interest and you want to calculate the amount that you will have after a specific
number of months. The formula is
F = P * (1 + i)^t
The terms in the formula are as follows:
• F is the future value of the account after the specified time period.
• P is the present value of the account.
• i is the monthly interest rate.
• t is the number of months.
Write a program that prompts the user to enter the account’s present value, monthly interest
rate, and number of months that the money will be left in the account. The program should
pass these values to a function that returns the future value of the account after the specified
number of months. The program should display the account’s future value.
"""

# function to start the program
def main():
	print()
	print("This program calculates future value of an account that earns compount monthly interest after number of months.")

	# get user input by calling the get_input function and assign the returned value to the appropirate variables
	present_value, monthly_interest, number_of_months = get_input()

	# call the future_value function to determine the future value
	f_value = future_value(present_value, monthly_interest, number_of_months)

	# display the future value
	print("The future value of your account after ", number_of_months, ' months is ', format(f_value,'.2f'))




# funcction to get user input
def get_input():
	# get the user input
	p_value = float(input("Please enter the present value: "))
	m_interest = float(input("Enter monthly interest. for 20 percent enter 0.2: "))
	n_months = int(input("Enter number of months: "))
	# return the above input to caller
	return p_value, m_interest, n_months
	# end of function


# fumction to calculate future value
def future_value(p, i, t):
	# calculate the future value using the formula
	print("present value = ", p)
	print("interest = ", i)
	print("number of months = ", t)
	f = p * ((1 + i) ** t)
	print(" 1 + i = ", 1 + i)
	print("(1 + i) ^2 = ", (1 + i) ** t)
	print(" p * (1 + i) ^2 = ", p * (1+i) ** t)
	print("f", f)

	# return the result
	return f
	# end of function


# call the main function
main()



