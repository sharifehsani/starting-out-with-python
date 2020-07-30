"""
- Author: Sharif Ehsani
- Date: July 27, 2020
- www.gitbuh.com/ehsanis

-This program displays a rectangular pattern of asterisks using the user input
"""

# main function to start the program
def main():
	print() # to make the code readable I always use a blank line to seperate the start and end of program from command line
	print("This program displays a rectangular pattern " +\
	"of asterisks using the user input.")

	# get user input
	rows = int(input("How many rows do you want in the rectangular? "))
	cols = int(input("How many columns do you want in the rectangular? "))

	# validate input to get positive number for number of rows and columns
	while (rows <= 0 or cols <= 0):
		print("ERROR!, rows and columns must be greater than zero. ")
		rows = int(input("How many rows do you want in the rectangular? "))
		cols = int(input("How many columns do you want in the rectangular? "))

	# call the pattern maker function and pass rows and cols as parameters
	pattern_maker(rows, cols)


# function to make rows and pattern
def pattern_maker(rows, cols):
	print()
	for each in range(rows):
		for other in range(cols):
			print("*", end="")
		print()
	print()

# call the main function
main()