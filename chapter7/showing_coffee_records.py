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
Your first job is to write a program that can be used to add records to the file. 
 Note that the output file is opened in append mode. Each time the
program is executed, the new records will be added to the file’s existing contents.

Your next job is to write a program that displays all of the records in the inventory file. 
"""

# function to start the program
def main():
	# open the file 'coffee_rocrds.txt'
	file_in = open('coffee_records.txt', 'r')

	# read the first line
	coffee_name = file_in.readline()

	# run a while loop until there is still data to be read
	while (coffee_name != ''):
		# read the quantity line and convert the quanting from string to float
		quantity = float(file_in.readline())

		# remove the new lines from the end of the lines
		coffee_name = coffee_name.rstrip('\n')
		# since float() method ignores the new line we don't need to remove the new line from the end
		#quantity = quantity.rstrip('\n')

		# display the records
		print("Discription: ", coffee_name)
		print("Quantity: ", quantity)
		# print a new line to devide the records
		print()

		# read the cofee name from the next record
		coffee_name = file_in.readline()

	# close the file
	file_in.close()

# call the main function
main()