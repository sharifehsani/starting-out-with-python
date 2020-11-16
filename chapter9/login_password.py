"""
- Author: Sharif Ehsani
- Date: September 2020
- www.gitbuh.com/ehsanis

In the Spotlight:
Validating the Characters in a Password
At the university, passwords for the campus computer system must meet the following
requirements:
• The password must be at least seven characters long.
• It must contain at least one uppercase letter.
• It must contain at least one lowercase letter.
• It must contain at least one numeric digit.
When a student sets up his or her password, the password must be validated to ensure it
meets these requirements. You have been asked to write the code that performs this validation.
You decide to write a function named valid_password that accepts the password as
an argument and returns either true or false, to indicate whether it is valid. Here is the algorithm
for the function, in pseudocode:
valid_password function:
Set the correct_length variable to false
Set the has_uppercase variable to false
Set the has_lowercase variable to false
Set the has_digit variable to false
If the password’s length is seven characters or greater:
Set the correct_length variable to true
for each character in the password:
if the character is an uppercase letter:
Set the has_uppercase variable to true
if the character is a lowercase letter:
Set the has_lowercase variable to true
if the character is a digit:
Set the has_digit variable to true
If correct_length and has_uppercase and has_lowercase and has_digit:
Set the is_valid variable to true
else:
Set the is_valid variable to false
Return the is_valid variable
Earlier (in the previous In the Spotlight section) you created a function named
get_login_name, and stored that function in the login module. Because the valid_password
function’s purpose is related to the task of creating a student’s login account, you
decide to store the valid_password function in the login module as well. Program 9-6
shows the login module with the valid_password function added to it.
"""

# main function to start the program
def main():

	# print the password minimum requirment and get users password
	print("Chooseing a strong password.")
	print("• The password must be at least seven characters long.")
	print("• It must contain at least one uppercase letter.")
	print("• It must contain at least one lowercase letter.")
	print("• It must contain at least one numeric digit.")
	

	# call the valid_password() function and pass the password to it as an argument
	# and assign the return result to the passowrd_is_valid boolean variable
	# in a whil loop keep asking the user for the right password until the right password is entered
	password_is_valid = False

	while (password_is_valid == False):
		password = input("Enter your password: ")
		password_is_valid = valid_password(password)
		if (password_is_valid == False):
			print("_____________Wrong type of Password_____________")
			print("Your password must be: ")
			print("• at least seven characters long.")
			print("• at least one uppercase letter.")
			print("• at least one lowercase letter.")
			print("• at least one numeric digit.")

	# print a message when the requirment is met and the password is set
	print("Success! your password is set")
	# print the last 3 character of the password for practice, the rest should be stars
	password_length = len(password) - 3
	print("Your password is: " ,"*" * password_length, password[-3:], sep='')
	
# functon to validate the password
def valid_password(password):

	# initialize follwoing boolean variables
	correct_length = False
	has_uppercase = False
	has_lowercase = False
	has_digit = False
	valid = False

	# check the lenght of the password to be at least 7 digit long
	if (len(password) >= 7):
		correct_length = True
	else:
		correct_length = False

	# chcek if the password has at least one lower_case letters, one upper case letter, has one digit 
	for ch in password:
		# check if the character in the password is lower case letter
		if (ch.islower()):
			has_lowercase = True

		# check if the character in the password is upper case letter
		if (ch.isupper()):
			has_uppercase = True

		# check if the character in the password is digit
		if (ch.isdigit()):
			has_digit = True

	# now check if all the conditions meet
	if (correct_length and has_lowercase and has_uppercase and has_digit):
		valid = True
	else:
		valid = False


	# return the result
	return valid




# call the main function
main()