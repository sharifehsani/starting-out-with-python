"""
- Author: Sharif Ehsani
- Date: July 2020
- www.gitbuh.com/ehsanis

2. Write a while loop that asks the user to enter two numbers. The numbers should be
added and the sum displayed. The loop should ask the user if he or she wishes to perform
the operation again. If so, the loop should repeat, otherwise it should terminate.
"""
# main function to start the program
def main():
	print()		# blanck line to seperate the program from the command line for readablity
	print("This program gets two numbers from the user, the program sums the two number up and dispay the sum "+ \
		"the program will ask the user if s/he wants to perform the operation again.")
	# call the get_input() function
	get_input()

# function to get user input
def get_input():
	perform_again = 'y'

	# ask the user if the s/he wants to perform the opeation again
	
	while (perform_again == 'y'):
		num_one = int(input("Enter the first number: "))
		num_two = int(input("Enter the second number: "))

		# validate the number if you want to work only with positive numbers
		# this is only for practice purpose
		"""
		while (num_one < 0  or num_two < 0):
			print("ERROR!, numbers must positive.")
			num_one = int(input("Enter the first number: "))
			num_two = int(input("Enter the second number: "))
		"""
		# call the sum_the_numbers() function and pass the numbers as parameters
		sum_the_numbers(num_one, num_two)
		# ask the user if they want to perform the operation again
		perform_again = input("Do you want to perform the operation again? press 'y' for yes: ")
		


# function to sum the two numbers
def sum_the_numbers(num_one, num_two):
	total = num_one + num_two
	print("Total of ", num_one, " + ", num_two, " = ", total)


# call the main function
main()
