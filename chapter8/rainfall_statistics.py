
"""
- Author: Sharif Ehsani
- Date: September 2020
- www.gitbuh.com/ehsanis

Programming Exercises
3. Rainfall Statistics
Design a program that lets the user enter the total rainfall for each of 12 months into a list. 
The program should calculate and display the total rainfall for the year, the average monthly rainfall, 
and the months with the highest and lowest amounts.
"""

# main function to start the program
def main():

	# initialize an accumulator to hold the total of the elements
	total = 0.0

	# initialize a list variable with 12 elements
	rainfall_list = [0] * 12
	# run the loop for 12 times = 12 month
	for month in range(12):
		# get user input and populate the list
		print("Enter the total rainfall for month ", month + 1, end='')
		rainfall_list[month] = float(input(": "))


	# in a loop add up all the elements of the list
	for num in rainfall_list:
		total += num

	# print the total
	print("Total rainfall for the year is: ", format(total, '.2f'))

	# print the average rainfall
	print("The average rainfall this year: ", format((total / 12), '.2f'))

	# print the month with the highest amount of rainfal
	print("The month with the highest rainfall amounth ", max(rainfall_list))

	# print the month with the lowest amount of rainfal
	print("The month with the lowest rainfall amounth ", min(rainfall_list))



# call the main function
main()
