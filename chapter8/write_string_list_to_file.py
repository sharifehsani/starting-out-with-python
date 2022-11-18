"""
- Author: Sharif Ehsani
- Date: September 2020
- https://github.com/sharifehsani

This program writes a list of strings to a file

"""

# function to start the program
def main():

	# creat a list of strings
	cities = ['Toronto', 'Vancouver', 'Calgary', 'Ottawa']

	# open a text file for output as 'w' access mode
	file_out = open('cities.txt', 'w')

	# in a loop write the list to the file
	for num in range(len(cities)):
		file_out.write(cities[num] + '\n')

	# close the file
	file_out.close()

	# print a message
	print("The list is written to file.")


# call the main function
main()
