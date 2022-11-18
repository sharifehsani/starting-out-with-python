"""
- Author: Sharif Ehsani
- Date: September 2020
- https://github.com/sharifehsani

Checkpoint
9.18 Assume the following statement appears in a program:
days = 'Monday Tuesday Wednesday'
Write a statement that splits the string, creating the following list:
['Monday', 'Tuesday', 'Wednesday']

"""

# main function to start the program
def main():

	# initialize a string variable
	days = 'Monday Tuesday Wednesday'

	# split the string frome the whitespace
	splited_string = days.split()

	# print the result
	print(splited_string)

# call the main function
main()
