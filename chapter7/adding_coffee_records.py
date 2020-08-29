"""
- Author: Sharif Ehsani
- Date: August 2020
- www.gitbuh.com/ehsanis

In the Spotlight:
Adding and Displaying Records
Midnight Coffee Roasters, Inc. is a small company that imports raw coffee beans from
around the world and roasts them to create a variety of gourmet coffees. Julie, the owner
of the company, has asked you to write a series of programs that she can use to manage her
inventory. After speaking with her, you have determined that a file is needed to keep inventory
records. 
Each record should have two fields to hold the following data:
• Description—a string containing the name of the coffee
• Quantity in inventory—the number of pounds in inventory, as a floating-point number
Your first job is to write a program that can be used to add records to the file. Program
7-15 shows the code. Note that the output file is opened in append mode. Each time the
program is executed, the new records will be added to the file’s existing contents.
"""

# main function to start the program
def main():

	# open a file in 'a' append mode and name it 'cofee_records.txt'
	file_out = open("coffee_records.txt", 'a')

	# a condition to keep the loop running
	keep_adding_more = 'y'

	# a while loop to run and get the user input and write to as long as keep_adding_more = 'y'
	while (keep_adding_more == 'y' or keep_adding_more == 'Y'):

		# get user input for coffee discription and quantity
		name_of_coffee = input("Enter the name of coffee: ")
		quantity = float(input("Enter the quantity in pounds: "))

		# write the info to the file
		file_out.write(name_of_coffee + '\n')
		file_out.write(str(quantity) + '\n')		# make sure you convert the floating point number to string first

		# ask the user if they have more cofee to add
		keep_adding_more = input("Do you want to add more coffee? 'y' for yes 'n' for now: ")

	# close the file
	file_out.close()
	print("The record is saved.")


# call the main function
main()