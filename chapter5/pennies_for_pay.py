"""
- Author: Sharif Ehsani
- Date: July 2020
- https://github.com/sharifehsani

7. Pennies for Pay
Write a program that calculates the amount of money a person would earn over a period
of time if his or her salary is one penny the first day, two pennies the second day, and
continues to double each day. The program should ask the user for the number of days.
Display a table showing what the salary was for each day, and then show the total pay at
the end of the period. The output should be displayed in a dollar amount, not the number
of pennies.
"""

# main function to start the program
def main():
	print()
	# display the program description
	print("This porgam calculates the amount of money a person would earn over a period of time if his/her salary is one penny the\n" +
		"first day, two pennies the second day, and continues to double each day. The program asks the user for the number of days.")
	total_pennies = 0
	
	#ask the user for the number of days
	number_of_days = int(input("Enter the number of days: "))
	salary = 1
	total_pennies = 0
	# display the reslut in a table
	print()
	print("Days \t\t Salary")
	print("---------------------------")

	for day in range(1, number_of_days + 1):
		total_pennies = total_pennies + salary
		
		if (day > 1):
			print("day", day,"\t\t$", salary, "Pennies")
		else:
			print("day", day,"\t\t$", salary, "Penny")

		salary = salary * 2
		# end of the loop

	total_dollar = total_pennies / 100

	print("Your total salary for the ", number_of_days, " days worked is $", format(total_dollar,'.2f'), sep='')
	print()


# call the main function
main()
