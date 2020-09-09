"""
- Author: Sharif Ehsani
- Date: August 2020
- www.gitbuh.com/ehsanis

This program ask the user how many sales item to add and gets sales amounts from the user and assigns them to a list.

"""

# function to start the program
def main():

	# creat a list variable the size of entry_count
	sales_list = []

	# use try suite and exception clauses
	try:
		# creat an output file
		file_out = open('sales_amounts.txt', 'w')

		# ask user about how many slaes entry to add
		entry_count = int(input("How many entries do you want to add: "))

		# in a for loop get user input and add to the list
		for count in range(1, entry_count + 1):
			# get user input for the sale
			sale = float(input("Enter sale amount: "))
			# add the sale amount to the list using the append method
			sales_list.append(sale)


		# write the sales_list to the file
		file_out.write(str(sales_list))

		# close the file
		file_out.close()

	# handle the exception raised
	except Exception as err:
		print(err)


# call the main function
main()





