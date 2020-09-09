"""
- Author: Sharif Ehsani
- Date: August 2020
- www.gitbuh.com/ehsanis

This program returns a reference of a list from a function
"""

# main function to start the program
def main():

	# call a function and get the list from it
	my_list = return_a_list()


	# print the list
	print("This is the list returned from the function: ", my_list)


# define a function to return a reference to a list that was created by the user
def return_a_list():

	# initialize an empty list
	student_list = []

	# a coditional variable for the loop
	more = 'y'

	# get user to populate the list
	while (more == 'y'):
		# get the name of the student
		name = input("Enter the name of the student: ")
		# append the name to the list
		student_list.append(name)
		# ask if the user wants to add more
		more = input("Do you want to add more students? 'y' for yes any key for no: ")

	# return the reference of the list to the caller
	return student_list


# call the main function
main()
