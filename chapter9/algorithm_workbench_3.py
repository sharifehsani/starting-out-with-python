"""
- Author: Sharif Ehsani
- Date: October 2020
- https://github.com/sharifehsani

Algorithm Workbench
3. Write a loop that counts the number of digits that appear in the string referenced by
mystring.

"""

# main function to start the program
def main():

	# creat a string that holds some digits
	my_string = 'number 20 devide by number 5 exactly 4 times'

	# creat a counter to hold the count of occuring digit
	count = 0

	# in a for loop iterate through the text and check each character for digit value
	for char in my_string:
		if char.isdigit():
			# whenever a digit is found increment the counter
			count += 1

	# print the result
	print("There are ", count, ' digits in the string: ', '"', my_string, '"', sep='')


# call the main function
main()
