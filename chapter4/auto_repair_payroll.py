"""
- Author: Sharif Ehsani
- Date: June 2020
- www.gitbuh.com/ehsanis

In the Spotlight:
Using the if-else Statement
Chris owns an auto repair business and has several employees. If any employee works over
40 hours in a week, he pays them 1.5 times their regular hourly pay rate for all hours over
40. He has asked you to design a simple payroll program that calculates an employee’s
gross pay, including any overtime wages. You design the following algorithm:
Get the number of hours worked.
Get the hourly pay rate.
If the employee worked more than 40 hours:
Calculate and display the gross pay with overtime.
Else:
Calculate and display the gross pay as usual.
Next, you go through the top-down design process (described in Chapter 3) and create the
hierarchy chart shown in Figure 4-9. As shown in the hierarchy chart, there are three functions,
summarized as follows:
"""

# main function to start the program
def main():
	intro_message()

# function to introduce the program
def intro_message():
	print("This payroll program calcualtes your pay including the overtime pay")
	get_input()

# function to get user input
def get_input():
	hours_worked = float(input("Enter the hours worked: "))
	hourly_pay_rate = float(input("Enter hourly pay rate: "))
	if (hours_worked > 40):
		calculate_with_overtime(hours_worked, hourly_pay_rate)
	else:
		calculate_usual(hours_worked, hourly_pay_rate)

# funcition to calculate overtime
def calculate_with_overtime(hours_worked, hourly_pay_rate):
	overtime_hours = hours_worked - 40
	gross_usual = 40 * hourly_pay_rate
	gross_overtime = overtime_hours * (1.5 * hourly_pay_rate)
	gross_total = gross_usual + gross_overtime
	print("Your worked hours = ", hours_worked)
	print("Your hourly_pay_rate = ", hourly_pay_rate)
	print("Your gross pay = $", format(gross_total, ',.2f'), sep='')
	print("Your overtime pay = $", format(gross_overtime, ',.2f'), sep='')


# function to calculate regular pay
def calculate_usual(hours_worked, hourly_pay_rate):
	gross_pay = hours_worked * hourly_pay_rate
	print("Your worked hours = ", hours_worked)
	print("Your hourly_pay_rate = ", hourly_pay_rate)
	print("Your gross pay = $", format(gross_pay, ',.2f'), sep='')


#call the main function	
main()