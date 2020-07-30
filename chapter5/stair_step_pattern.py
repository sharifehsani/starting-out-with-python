"""
- Author: Sharif Ehsani
- Date: July 2020
- www.gitbuh.com/ehsanis

- This program prints a stair step patther using nested loop
"""

# main function to start the program
def main():
	print()		# print a blank line to seperate the start of the program form the command line
	print("This program prints a stair step patther using nested loop.")
	get_input()	# call the get_input function

# function to get user input
def get_input():
	# ask the user to choose the size of the pattern
	size_of_pattern = int(input("How many rows of pattern do you want to have: "))

	# validate the user input to make sure invalid input is not given
	while(size_of_pattern <= 1):
		print("ERROR!, size of the pattern must be greater than one.")
		size_of_pattern = int(input("How many rows of pattern do you want to have: "))

	# call the make_pattern() function and pass size_of_pattern as parameter
	make_pattern(size_of_pattern)

# functoin to make the pattern
def make_pattern(size_of_pattern):
	for r in range(size_of_pattern):
		for c in range(r + 1):
			print(" ", end='')	# print spaces afte each other in the same line
		print("#")				# print a # at the end of the inner loop each time the loop ends which also adds a news line after it


# call the main function
main()