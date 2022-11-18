"""
- Author: Sharif Ehsani
- Date: October 2020
- https://github.com/sharifehsani

Algorithm Workbench
5. Write a function that accepts a string as an argument and returns true if the argument
ends with the substring '.com'. Otherwise, the function should return false.
"""

# main function to start the prgogram
def main():

	# get user input
	my_string = input("Enter your favourait website: ")

	# call the function and pass the string to it as an argument
	result = check_substring(my_string)

	# print the result of the function call
	if result == True:
		print("Your website ends with '.com'")
	else:
		print("Your favourait website does not end with '.com'")

# define a function to check the substring for '.com'
def check_substring(my_str):
	# initite a boolean variable to hold the status the string
	outcome = False

	# check if '.com' exist at the end of the string, if so make the outcome True
	if my_str.endswith('.com'):
		outcome = True;

	# return the outcome to the caller
	return outcome



# call the main function
main()


