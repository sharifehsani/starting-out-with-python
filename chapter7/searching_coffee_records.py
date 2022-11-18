"""
- Author: Sharif Ehsani
- Date: August 2020
- https://github.com/sharifehsani

In the Spotlight:
Searching for a Record
Julie has been using the first two programs that you wrote for her. She now has several
records stored in the coffee_records.txt file, and has asked you to write another program that she
can use to search for records. She wants to be able to enter a description and see a list of
all the records matching that description.
"""

# main function to start the prgoram
def main():
	match_found = False
	count = 0

	# get the user input about the search criteria
	search_for = input("Enter the name or discription of the coffee to search: ")
	# open the 'coffee_records.txt' file in 'r' access mode
	file_in = open('coffee_records.txt', 'r')

	# read the first line

	coffe_name = file_in.readline()

	# in a loop read all the lines untill the last
	while (coffe_name != ''):
		# read the next line and convert it to floating point
		coffee_quantity = float(file_in.readline())

		# remove the new line from the end of the line
		coffe_name = coffe_name.rstrip('\n')
	

		# match the searched coffee with cofee name
		if (search_for == coffe_name):
			print("Coffe name: ", coffe_name)
			print("Quantity: ", coffee_quantity)
			match_found = True

		# read the next line
		coffe_name = file_in.readline()

	# print the following if match not found
	if not match_found:
		print("Match not fount.")
	# close the file
	file_in.close()


# call the main function
main()

