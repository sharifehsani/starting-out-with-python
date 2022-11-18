"""
- Author: Sharif Ehsani
- Date: September 2020
- https://github.com/sharifehsani

This program reads a list of strings from a file

"""

# function to start the program
def main():

	# creat a list variable to write the data read from the file
	canadaian_cities = []
	# open the file for reading in a try suite and except clause 
	try:
		fil_in = open('cities.txt', 'r')

		# in a loop read each line of the file
		for line in fil_in:
			# assign each line to a variable
			name = line
			# strip the new line from the end of each line
			name = name.rstrip('\n')

			# write  the line read to the list
			canadaian_cities.append(name)

		# close the file
		fil_in.close()

		# print the list
		print("The following data was read from the file.")
		print(canadaian_cities)


	# handle the exception raised
	except Exception as err:
		print("An error happened while trying to open or read file. ", err)


# call the main function
main()
