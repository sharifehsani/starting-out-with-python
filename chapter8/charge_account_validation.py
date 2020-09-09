"""
- Author: Sharif Ehsani
- Date: September 2020
- www.gitbuh.com/ehsanis

Programming Exercises
5. Charge Account Validation
If you have downloaded the source code from this book’s companion Web site, you will find a file named 
charge_accounts.txt in the Chapter 08 folder. This file has a list of a company’s valid charge account numbers. 
Each account number is a seven-digit number, such as 5658845.
Write a program that reads the contents of the file into a list. The program should then ask the user to enter 
a charge account number. The program should determine whether the number is valid by searching for it in the list. 
If the number is in the list, the program should display a message indicating the number is valid. If the number is 
not in the list, the pro- gram should display a message indicating the number is invalid.
"""

# main function to start the program
def main():


	# since we don't have access to the source code, 'charge_accounts.txt' file does not exist
	# so lets manually creat a file with 10 accounts
	
	# open the file in a try suite and excpet clause
	try:

		file_in = open('charge_accounts.txt', 'r')
		# initialize an empty list variable
		charge_account_number_list = []

		# read the content of the file into a list
		for line in file_in:
			# convert the string to int value before writting it to the list
			charge_account_number_list.append(int(line))

		print(charge_account_number_list)

		# close the file
		file_in.close()

		# ask the user to enter a charge account number to search
		charge_account_number = int(input("Enter a charge account number to search: "))

		# check if the charge account number exist in the list or not and print a message in each case
		if charge_account_number in charge_account_number_list:
			print("The account number is valide.")

		else:
			print("The account number is invalide.")

	except Exception as err:
		print("An error occured. ", err)

# call the main function
main()
