"""
- Author: Sharif Ehsani
- Date: September 2020
- https://github.com/sharifehsani

This program reads some random integer numbers from file and creats a list of the int numbers

"""

# main function to start the program
def main():

	# creat and initialize the list
	random_numbers_list = []
	try:
		# open the file in 'r' access mode
		file_in = open("random_numbers.txt", 'r')

		# read the data from the file in a loop
		for line in file_in:
			# int() method discards the new line character from the end of the line while converting to int
			num = int(line)
			# append each number read to the list
			random_numbers_list.append(num)


		# close the file
		file_in.close()

		# print message
		print('The data is read from file and written to a list.')
		print("Here is the list: ", random_numbers_list)
	# catch the exceptions raised
	except Exception as err:
		print("Error occured: ", err)


# call the main function
main()
