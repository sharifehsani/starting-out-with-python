"""
- Author: Sharif Ehsani
- Date: July 2020
- https://github.com/sharifehsani

5. Average Rainfall
Write a program that uses nested loops to collect data and calculate the average rainfall
over a period of years. The program should first ask for the number of years. The
outer loop will iterate once for each year. The inner loop will iterate twelve times, once
for each month. Each iteration of the inner loop will ask the user for the inches of rainfall
for that month. After all iterations, the program should display the number of
months, the total inches of rainfall, and the average rainfall per month for the entire
period.
"""

# main function to start the program
def main():
	print()
	print('This program calculates the average rainfall over a period of years.')
	# call get_input() function to get user input
	get_input()

# function to get user input
def get_input():
	# ask user to enter the number of years
	number_of_years = int(input("Enter number of years: "))
	

	# List has not been covered so far, but I use list to make getting input from the user be fancier
	# You can ignore line 31 and 40 if you have not heard of list to avoid confusion. and add regual message inside the input()
	# You can also chagne the inner for loop to "for month in range(1, 13) or anything to make it run 12 times"
	month_of_the_year = ["January", "February", "March", "April", "May", "June", "July", "August", "Septerber", "October", "November", "December"]
	
	# accumolators
	total_rainfall = 0.0
	number_of_months = 0
	average_rainfall = 0.0

	# nested for loop to ask the user inches of rainfall for each month of the year
	for year in range(1, number_of_years + 1):
		print("year ", year, ' rainfall amount: ')
		print("----------------------------------")
		# the inner loop should run 12 times
		for month in month_of_the_year:
			print("Enter the inches of rainfall for the month of ", month,": ", sep='', end='')
			# this input has no message in it, but will apear at the end of print statement above this line
			rainfall_in_each_month = float(input())
			number_of_months = number_of_months + 1
			total_rainfall = total_rainfall + rainfall_in_each_month
		print()	

	average_rainfall = total_rainfall / number_of_months	
	print("Total number of Months = ", number_of_months)
	print("Total inches of rainfall during the entire period = ", format(total_rainfall, ".2f"), "Inches.")	
	print("Average rainfall per month for the entire duration = ", format(average_rainfall, '.2f'), "Inches")
	

# call the main function
main()


