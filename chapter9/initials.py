"""
- Author: Sharif Ehsani
- Date: October 2020
- www.gitbuh.com/ehsanis

Programming Exercises
1. Initials
Write a program that gets a string containing a person’s first, middle, and last names, and
then display their first, middle, and last initials. For example, if the user enters John
William Smith the program should display J. W. S.

"""

# main function to start the program
def main():

	# get user input
	f_name = input("Enter you first name: ")
	m_name = input("Enter your middle name: ")
	l_name = input("Enter your last name: ")


	# get the first letters of the user's first, middle and alst name and convert them to uppercase
	f_initial = f_name[0]
	m_initial = m_name[0]
	l_initial = l_name[0]

	# conver them to uppercase letter
	f_initial = f_initial.upper()
	m_initial = m_initial.upper()
	l_initial = l_initial.upper()

	# print the result with '. ' in between
	space = '. '

	print(f_initial, space, m_initial, space, l_initial, space, sep='')


# call the main function
main()
	
