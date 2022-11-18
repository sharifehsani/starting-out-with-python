"""
- Author: Sharif Ehsani
- Date: September 2020
- https://github.com/sharifehsani

This program writes generates a list of random numbers between 1 and 10 and writes the list of numbers to a file

"""

# improt random module from standard python library
import random

# main function to start the program
def main():

	# creat and initialize a list variable
	random_numbers_list = []

	# do the code in a try suite
	try:
		# creat a list of  10 random int numbers between 1 and 10
		# make sure you import random module from the standard python library
		for num in range(1, 11):
			# generate random int between 1 and 10 and assign it to number variable
			number = random.randint(1, 10)
			print(number)
			# write the generated number to the list
			random_numbers_list.append(number)
		
		# in another for loop write the elements of the list to the file
		# creat/open an output file in 'w' access mode
		file_out = open('random_numbers.txt', 'w')

		# writ to file
		for num in range(len(random_numbers_list)):
			# convert the int to string before writting to file and also add new line at the end of each line
			file_out.write(str(random_numbers_list[num]) + '\n')

		# close the output file
		file_out.close()

		# print a message
		print("The lis of randome number is written to file succuessfully.")

	# in an except clause write the type of possible error type
	except Exception as err:
		print("an error occured. ", err)

# call the main function
main()
