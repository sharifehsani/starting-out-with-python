"""
- Author: Sharif Ehsani
- Date: August 2020
- www.gitbuh.com/ehsanis

In the Spotlight:
Using List Elements in a Math Expression
Megan owns a small neighborhood coffee shop, and she has six employees who work as baristas (coffee bartenders). 
All of the employees have the same hourly pay rate. Megan has asked you to design a program that will allow her to enter the 
number of hours worked by each employee and then display the amounts of all the employees’ gross pay. You determine that the 
program should perform the following steps:

1. For each employee: get the number of hours worked and store it in a list element.
2. For each list element: use the value stored in the element to calculate an employee’s
gross pay. Display the amount of the gross pay.
"""

# main function to start the program
def main():

	# ask the user to input the number of employees. this specify the size of the list
	number_of_employees = int(input("Enter the number of employees: "))

	# creat a list the size of number of employees
	hourse_worked = [0] * number_of_employees

	# in a loop get hours worked for each employee and put it in the list
	for num in range(1, number_of_employees + 1):
		print("Enter hours worked for employee ", num , ': ', sep='', end='')
		# get the number of hours worked
		number_of_hours = float(input())
		# enter the hours worked in the list
		hourse_worked[num - 1] = number_of_hours


	# get hourly rate
	hourly_rate = float(input("Enter hourly rate: "))

	# in a loop calculate the gross pay for each worker and print
	for index in range(len(hourse_worked)):
		# calculate the gross pay my multiplying 
		gross_pay = hourse_worked[index] * hourly_rate
		print("Gross pay for employee ",  index + 1, ": $", format(gross_pay, '.2f'), sep='')
	


# call the main function
main()

