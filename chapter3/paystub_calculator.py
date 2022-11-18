"""
- Author: Sharif Ehsani
- Date: June 2020
- https://github.com/sharifehsani

When using functions in a program, you generally isolate each task within the program in
its own function. For example, a realistic pay calculating program might have the following
functions:
• A function that gets the employee’s hourly pay rate
• A function that gets the number of hours worked
• A function that calculates the employee’s gross pay
• A function that calculates the overtime pay
• A function that calculates the withholdings for taxes and benefits
• A function that calculates the net pay
• A function that prints the paycheck
A program that has been written with each task in its own function is called a modularized
program.
"""


# main function

def main():
	print()
	print("This program calculates your gross pay, taxes, benifits and net pay:")
	get_hourly_payrate() # call get_hourly_payrate() function
	

# • A function that gets the employee’s hourly pay rate
def get_hourly_payrate():

	hourly_pay_rate = float(input("Please enter your hourly pay rate: "))
	get_hours_worked(hourly_pay_rate) # call the get_hours_worked() function and pass hourly_pay_rate as parameter

# • A function that gets the number of hours worked
def get_hours_worked(hourly_pay_rate):
	wage = hourly_pay_rate
	hours_worked = float(input("Enter total hours worked: "))
	if (hours_worked > 87):
		overtime_pay = calculate_overtime_pay(wage, hours_worked)
		calculate_gross_pay(wage, hours_worked, overtime_pay)
	else:
		overtime_pay = 0
		calculate_gross_pay(wage, hours_worked, overtime_pay)

# • A function that calculates the overtime pay
def calculate_overtime_pay(wage, hours_worked):
	overtime_hour = hours_worked - 87
	overtime_pay = overtime_hour * (wage + (wage / 2))
	return overtime_pay # return to caller
	


# • A function that calculates the gross pay
def calculate_gross_pay(wage, hours_worked, overtime_pay):
	total_pay = (wage * hours_worked) + overtime_pay
	union_dues = total_pay * 0.03946491
	gross_pay = total_pay - union_dues
	print()
	print("Here is how your paystub looks like:")
	print("Total hourse worked: ", format(hours_worked, '.2f'))
	print("Hourly pay rate: ", format(wage, '.2f'))
	print("Pre-tax duduction, union dues: ", format(union_dues,'.2f'))
	print("Gross pay: ", format(gross_pay, '.2f'))

	calculate_tax_benifit(gross_pay)
	


# • A function that calculates the withholdings for taxes and benefits
def calculate_tax_benifit(gross_pay):
	# taxes

	federal_income_tax = gross_pay * 0.04703797
	provincial_income_tax = gross_pay * 0.00452657
	total_tax = federal_income_tax + provincial_income_tax

	# benifits
	canada_pension_plan = 0.04618774 * gross_pay
	employment_insurance = 0.01645371 * gross_pay
	print("Federal Income Tax: ", format(federal_income_tax, '.2f'))
	print("provincial Income Tax", format(provincial_income_tax, '.2f'))
	print("Canada Pension Plan: ", format(canada_pension_plan,'.2f'))
	print("Employment Insurance: ", format(employment_insurance, '.2f'))

	calculate_net_pay(gross_pay, total_tax, canada_pension_plan, employment_insurance)

	

# • A function that calculates the net pay
def calculate_net_pay(gross_pay, total_tax, canada_pension_plan, employment_insurance):
	net_pay = gross_pay - (total_tax + canada_pension_plan + employment_insurance)

	print_paycheck(net_pay)


# • A function that prints the paycheck

def print_paycheck(net_pay):
	print("Your Net Pay is: ", format(net_pay, '.2f'))



# Call main function

main()
