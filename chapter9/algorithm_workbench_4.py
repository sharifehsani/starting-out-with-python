"""
- Author: Sharif Ehsani
- Date: October 2020
- https://github.com/sharifehsani

Algorithm Workbench
4. Write a loop that counts the number of lowercase characters that appear in the string
referenced by mystring.

"""

# main function to start the program
def main():

	# creat a string that holds some lower case letters
	my_string = "Hello World! is a very famouse Programing expression"

	# create a counter to hold the count of occuring lowercase letter
	count = 0

	# loop through the string and check each character for lowercase condition
	for ch in my_string:
		if ch.islower():

			count += 1

	print(count, "lowercase letter exist in the string: ", '"', my_string, '"')


# call the main function
main()
