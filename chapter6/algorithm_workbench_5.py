"""
- Author: Sharif Ehsani
- Date: July 2020
- www.gitbuh.com/ehsanis

5. Write a function named get_first_name that asks the user to enter his or her first
name, and returns it.
"""

# main function to start the program
def main():
	print()
	print("This program asks the user to enter his/her first name and returns the value to main.")
	# call the get_first_name() function and assign the returned value to a f_name variable
	f_name = get_first_name()

	# print the returned value
	print("Your first name is: ", f_name)


# function to get user's first name
def get_first_name():
	# get the user's first name
	first_name = input("Enter your first name: ")
	# return it to the caller
	return first_name



# call the main function
main()