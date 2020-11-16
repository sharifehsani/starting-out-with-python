
"""
- Author: Sharif Ehsani
- Date: September 2020
- www.gitbuh.com/ehsanis

In the Spotlight:
Extracting Characters from a String
At a university, each student is assigned a system login name, which the student uses to log
into the campus computer system. As part of your internship with the university’s Information
Technology department, you have been asked to write the code that generates system login
names for students. 

You will use the following algorithm to generate a login name:

1. Get the first three characters of the student’s first name. (If the first name is less than
three characters in length, use the entire first name.)
2. Get the first three characters of the student’s last name. (If the last name is less than
three characters in length, use the entire last name.)
3. Get the last three characters of the student’s ID number. (If the ID number is less than
three characters in length, use the entire ID number.)
4. Concatenate the three sets of characters to generate the login name.
For example, if a student’s name is Amanda Spencer, and her ID number is ENG6721, her
login name would be AmaSpe721. You decide to write a function named get_login_name
that accepts a student’s first name, last name, and ID number as arguments, and returns the
student’s login name as a string. You will save the function in a module named login.py.
This module can then be imported into any Python program that needs to generate a login
name.
"""

# import the login module created to work with this program, so it generates a log in name
import login

# main function to start the program
def main():

	# get student's first and last name and student ID
	first_name = input("Enter your first name: ")
	last_name = input("Enter your last name: ")
	student_id = input("Enter your student ID: ")

	# cal the get_login_name() method and pass the first, last name and id as arguments
	# and assign the returned value to login_name variable
	# use the import statement to use the imported module
	
	login_name = login.get_login_name(first_name, last_name, student_id)

	# print the login_name
	print("Here is your login_name: ", login_name)


# call the main function
main()