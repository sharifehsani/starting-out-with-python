"""
- Author: Sharif Ehsani
- Date: June 2020
- https://github.com/sharifehsani

- This program gets the user to creat a profile (username and password)
"""
# Function proglog to start the program
USER_NAME = ''
PASSWORD = ''
def main():
	print()
	display_message()


# function to display intro message
def display_message():
	print("Lets creat you a new account and login information. Please fill in the following information.")
	get_input()

# function to get user input
def get_input():
	first_name = input("First name: ")
	last_name = input("Last name: ")
	USER_NAME = input('User name: ')
	PASSWORD = input("Password: ")
	print("Thank you", first_name, last_name, "Your account is now set.")
	
	log_in(USER_NAME, PASSWORD)

def log_in(USER_NAME, PASSWORD):
	print("Let's now log you in: ")
	user_name = input("Enter your user name: ")
	password = input("Enter your user password: ")
	if (USER_NAME == user_name and PASSWORD == password):
		print("Access granted! you are now in.")
	else:
		print("Either your user name or password is incorrect. ")
		print("Please try again.")
		log_in(USER_NAME, PASSWORD)
	print()

main()
