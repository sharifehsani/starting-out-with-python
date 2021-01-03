"""
- Author: Sharif Ehsani
- Date: December 2020
- www.gitbuh.com/ehsanis

Programming Exercises
8. Name and Email Addresses
Write a program that keeps names and email addresses in a dictionary as key-value pairs.
The program should display a menu that lets the user look up a person’s email address, add
a new name and email address, change an existing email address, and delete an existing
name and email address. The program should pickle the dictionary and save it to a file
when the user exits the program. Each time the program starts, it should retrieve the dictionary
from the file and unpickle it.
"""

# import pickle module
import pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# menue function
def menue(user_choice):
	
	print()
	print(".....You are in the main menue.....")
	print("Select from the following options.")
	print("Look up a person's email address: 1")
	print("Add new names and emails address: 2")
	print("Change an existing email address: 3")
	print("Delete and existing name and email: 4")
	print("Exist the program: 5")

	# get user input for the menue option and run the loop until the user selects quit
	user_input = int(input("Your selection: "))
	while ((user_input > QUIT) & (user_input < LOOK_UP)):
		user_input = int(input("Select one of the above options: "))

	# return user input to the main function
	return user_input
	

# functio search for the email address in the existing file
def look_up(name_email_dic):
	# print some infor to let the user know about the current menue selection
	print()
	print(".....You are in the look up menue.....")
	print("Enter a name to display the email address: ")
	# declare a counter variable to control the loop for letting the user keep looking until the
	# user does not want to anymore
	more = 'y'
	while (more == 'y'):
		name = input("Name: ")
		if (name in name_email_dic):
			print("Emial:", name_email_dic[name])
		else:
			print("Oops!", name, "does not exist.")
		more = input("Do you want to look up more email address? 'y/n: ")


# function to allow the user to add new name and email address to the list
def add(name_email_dic):
	# open the file for adding
	file_in = open("name_email.dat", 'ab')
	# print some infor to let the user know about the current menue selection
	print()
	print(".....You are in the add email menue.....")
	print("Enter a name and a corresponding email address: ")
	# declare a counter to control the loop
	more = 'y'
	# in a loop keep adding name to the list until the user doesn't want to anymore
	while(more == 'y'):
		# get user input
		name = input("Name: ")
		# check if name already exist
		while (name in name_email_dic):
			print(name, "already exist.")
			name = input("Enter another name: ")
			
		email = input("Email:")
		# chek if email is already taken
		while (email in name_email_dic):
			print(email, "already exist. Enter another email:")
			email = input("Enter another email: ")
		# add the name and email address to the dictionary
		name_email_dic[name] = email
		more = input("Do you want to add more? 'y/n: ")
	# write to file
	pickle.dump(name_email_dic, file_in)

	#close the file
	file_in.close()

# function to change 
def change(name_email_dic):
	# print some infor to let the user know about the current menue selection
	print()
	print(".....You are in change email menue.....")
	print("Whose email address you want to change? ")
	# open the file
	file_in = open("name_email.dat", "ab+")
	# declare a counter to control the loop
	more = 'y'
	while (more == 'y'):
		name = input("Name: ")
		while (name not in name_email_dic):
			print(name, "does not exist.")
			name = input("Enter the correct name: ")
		print("Enter new email for", name, end='')
		new_email = input(": ")
		name_email_dic[name] = new_email
		more = input("Do you want to change more? 'y/n': ")
	# write back to file
	pickle.dump(name_email_dic, file_in)

	# close file
	file_in.close()

# function to delet existing email address
def delete(name_email_dic):
	# open file in append mode
	file_in = open('name_email.dat', 'ab+')
	# print some info to let the user know about the current menue selection
	print()
	print(".....You are in change email menue.....")
	print("Whose email address you want to delete? ")
	# declare a counter variable to control the loop
	more = 'y'
	# in a loop keep deleting until the user selects otherwise
	while (more == 'y'):
		name = input("Name: ")
		while (name not in name_email_dic):
			print(name, 'does not exist.')
			name = input("Enter another name: ")

		del name_email_dic[name]
		print(name, "deleted.")
		more = input("Do you want to delete more? 'y/n': ")
	# write the dictionary back to file
	pickle.dump(name_email_dic, file_in)





# function to creat a file, open the file and write the dictionary to it

# main function to start the program
def main():
	# declare a dictionary variable
	name_email_dic = {}

	# open the file to retrieve the names and email addresses and put it in a dictionary
	# in read and write format
	# make sure picke module is imported
	file_in = open('name_email.dat', 'rb')
	# declare an end_of_file variable to find the end of file
	end_of_file = False
	# in a loop read the content of the file until the end of file is reached
	while not end_of_file:
		# in a try and except clause read unpickle the file and assign the content to dictionary variable
		try:
			name_email_dic = pickle.load(file_in)
		
		except EOFError:
			end_of_file = True
	# close the file once read
	file_in.close()

	# call the appropriate functin when the user selects one and pass the dictoinary as argument
	user_choice = 0
	while (user_choice != QUIT):
		user_choice = menue(user_choice)
		if (user_choice == 1):
			look_up(name_email_dic)
		elif (user_choice == 2):
			add(name_email_dic)
		elif (user_choice == 3):
			change(name_email_dic)
		elif (user_choice == 4):
			delete(name_email_dic)

	print("Bye bye!")

	





# call the main function
main()