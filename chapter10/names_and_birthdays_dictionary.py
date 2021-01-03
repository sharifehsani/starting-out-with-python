"""
- Author: Sharif Ehsani
- Date: November 2020
- www.gitbuh.com/ehsanis

In the Spotlight:
Storing Names and Birthdays in a Dictionary
In this section we look at a program that keeps your friends’ names and birthdays in a dictionary.
Each entry in the dictionary uses a friend’s name as the key and that friend’s birthday
as the value. You can use the program to look up your friends’ birthdays by entering
their names.
The program displays a menu that allows the user to make one of the following choices:
1. Look up a birthday
2. Add a new birthday
3. Change a birthday
4. Delete a birthday
5. Quit the program
The program initially starts with an empty dictionary, so you have to choose item 2 from
the menu to add a new entry. Once you have added a few entries, you can choose item 1 to
look up a specific person’s birthday, item 3 to change an existing birthday in the dictionary,
item 4 to delete a birthday from the dictionary, or item 5 to quit the program.
Program 10-2 shows the program code. The program is divided into six functions: main,
get_menu_choice, look_up, add, change, and delete. Rather than presenting the entire
program at once, let’s first examine the global constants and the main function:
"""
# Glogal constant variables
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
SHOW = 5
QUIT = 6

# get menu choice function that gets user input
def get_menu_choice():

	# print the menue options
	print()
	print("YOU ARE AT THE MAIN MENU:")
	print("Please make one of the following choices:")
	print("1. Look up a birthday.")
	print("2. Add a new birthday.")
	print("3. Change a birthday.")
	print("4. Delete a birthday.")
	print("5. Show the names.")
	print("6. Quit the program.")



	# get user input for one of the 6 options
	user_input = int(input("Please enter a value between 1 and 6: "))
	# create a while loop that runs as long as the user inputs the right input(between 1 and 5)
	while ((user_input < LOOK_UP) or (user_input > QUIT)):
		print("Error!, Wrong input.")
		user_input = int(input("Please enter a value between 1 and 6: "))

	# return the user's input to the caller
	return user_input


# look up function to let user check 
def look_up(birthdays):
	print()
	# check if the dictionary is empty by using not boolean value
	empty = not birthdays
	if (empty == True):
		print("Your frinds' birthday list is empty.")
		print("You can add to the list by choosing option 2 from the main menu.")
	else:
		# search the dictionary to find the value, use a loop to allow the user keep searching
		keep_going = 'y'
		while (keep_going == 'y'):
			name = input("Enter your friend's name to search: ").lower()
			# if the name is not in the dictionary, let the user know and get another input
			while (name not in birthdays):
				print(name, "does not exist.")
				name = input("Enter your friend's name to search: ").lower()
			# print the value of the key requested
			print(name, "'s birthday is ", birthdays.get(name), sep='')
			# ask the user if s/he wants to keep searching
			keep_going = input("Do you want to search for another friend's birthday? yes = 'y', no = 'n': ").lower()



# function to add new elements to the dictionary
def add(birthdays):
	# add elements to the dictionary
	# in a loo get user input for the the key and value as long as has elements to add
	print()
	# let the user keep adding untile s/he does not want to add anymore
	keep_going = 'y'
	# the while loop runs until the condition changes
	while (keep_going == 'y'):					
		name = input("Enter firend's name: ").lower()
		# check if the key is already in the dictionary and let the user know
		# since you can't have duplicate key in a dictionary
		while (name in birthdays):
			print("Name already exist. Add another name.")
			name = input("Enter firend's name: ").lower()
		b_day = input("Enter friend's birthday: ")
		# convert the user input to lower case before checking
		keep_going = input("Do you want to continue? yes = 'y' or no = 'n': ").lower()
		# check if the key is already in the dictionary

		# add the element to the dictionary
		birthdays[name] = b_day					

		print("Your frind's birthday is added.")	
	return birthdays 			# return the dictionary

# function to change the elements of the dictionary
def change(birthdays):
	# change the elements of the dictionary
	# get the key that needs to be changed from the user
	print()
	# check if the dictionary is empty and notifu user if so
	empty = not birthdays
	if (empty == True):
		print("Your frinds' birthday list is empty.")
		print("You can add to the list by choosing option 2 from the main menu.")
	# if the dictionary is not empty let user keep changing until they don't want anymore
	else:
		keep_going = 'y'
		while (keep_going == 'y'):
			name = input("Which frind's birthday do you want to change? ").lower()
			# check if the name (key) exist
			while (name not in birthdays):
				print(name, "does not exist.")
				name = input("Enter another name: ").lower()
			new_birthday = input("Enter birthday: ").lower()
			birthdays[name] = new_birthday
			keep_going = input("Do you want to change more birthdays? yes = 'y', no = 'n': ").lower()
			print("Your friend's birthday list is updated.")
	return birthdays


# function to delet elements of the dictionary
def delete(birthdays):
	print()
	# check if the dictionary is empty, if so let the user know
	empty = not birthdays
	if (empty == True):
		print("Your frinds' birthday list is empty.")
		print("You can add to the list by choosing option 2 from the main menu.")
	# delete the elements of the dictionary
	# keep the user in the loop to delete as long as the user does not want to delete anymore
	else:
		keep_going = 'y'
		while (keep_going == 'y'):
			delete_name = input("Whic friend's birthday do you want to delete from the list? ").lower()
			# check if the key exist
			while (delete_name not in birthdays):
				print("This name does not exist.")
				delete_name = input("Enter another name ").lower()
			birthdays.pop(delete_name)
			print(delete_name, "deleted.")
			keep_going = input("Do you want to delete more birthdays? yes = 'y', no = 'n': ").lower()
			print("Your friend's birthday list is updated.")
		
	return birthdays

# function to display the friends' birthday list
def show(birthdays):
	print()
	# print the birthday list
	# check if the list is empty, if so let the suer know
	empty = not birthdays
	if empty == True:
		print("Your frinds' birthday list is empty.")
		print("You can add to the list by choosing option 2 from the main menu.")
	else:
		print()
		print("Here is your frind's birthday list:", birthdays)
	

# main function to start the program
def main():
	
	# initialize an empty dictionary
	birthdays = {}

	# initialize a variable to hold the user's choice
	user_choice = 0

	# this menue should be running until the user chooses to quit the program
	# so use a while loop to run as long as quit command is false
	while (user_choice != QUIT):
		user_choice = get_menu_choice()		# call the get_menu_choice function and assign the returned value to user_choice
		if (user_choice == LOOK_UP):
			look_up(birthdays)
		elif (user_choice == ADD):
			add(birthdays)
		elif (user_choice == CHANGE):
			change(birthdays)
		elif (user_choice == DELETE):
			delete(birthdays)
		elif (user_choice == SHOW):
			show(birthdays)

	print()
	print(birthdays)

# call the main function
main()