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


# this is the method that generates the login_name saved as python module, this can be imported to 
# any program to work. we will use it in the generate_goin_name.py program

# function to get the student's login name
def get_login_name(fname, lname, s_id):

	# initialize variables for the three sets of character that we get from first name, last name and id
	first_name_char = ''
	last_name_char = ''
	id_char = ''

	# initialize the login_name variable
	log_in_name = ''

	# check the length of the first name
	# if the first name is less than 3 character, let the first set of character be the whole first name
	if (len(fname) < 3):
		first_name_char = fname
	# if the length of first name is greater than or equal to three chracter, then take th first 3 character
	else:
		first_name_char = fname[0: 4]

	# check the length of the first name
	# if the last name is less than 3 character, let the second set of character be the whole last name
	if (len(lname) < 3):
		last_name_char = lname
	# if the length of last name is greater than or equal to three chracter, then take th first 3 character
	else:
		last_name_char = lname[0: 4]

	# check the length of the student ID
	# if the length of student id is less than 3 character, let the third set of character be the whole id
	if (len(s_id) < 3):
		id_char = s_id
	# if the length of student id is greater than or equal to three chracter, then take th last 3 character
	else:
		id_char = s_id[-3:]

	# concatinate all three sets of character that is taken from first name, last name and student id
	log_in_name = first_name_char + last_name_char + id_char

	# return the login name
	return log_in_name


