"""
- Author: Sharif Ehsani
- Date: September 2020
- https://github.com/sharifehsani

Programming Exercises
4. Number Analysis Program
Design a program that asks the user to enter a series of 20 numbers. The program should store 
the numbers in a list and then display the following data:
• The lowest number in the list
• The highest number in the list
• The total of the numbers in the list
• The average of the numbers in the list
"""

# main function to start the program
def main():

	# initialize the list variable with 20 elements using the repition operator
	numbers_list = [0] * 20

	# in a loop that runs 20 times ask the user to populate the list
	print("Enter a total of 20 numbers.")
	for num in range(len(numbers_list)):
		print("Enter number ", num + 1, end='')
		numbers_list[num] = int(input(": "))


	# print the lowest number in the list
	print("The lowest number in the list = ", min(numbers_list))

	# print the highest number in the list
	print("The highest number in the list = ", max(numbers_list))

	# print the total of the numbers
	total = 0
	for num in numbers_list:
		total += num

	print("The total of all the numbers in the list = ", total)


	# print the average of the numbers in the list
	print("The average of all the numbers in the list = ", total / 20)





# call th main function
main()
