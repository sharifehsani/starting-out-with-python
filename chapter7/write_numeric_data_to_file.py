"""
- Author: Sharif Ehsani
- Date: August 2020
- www.https://github.com/sharifehsani


This program writes numeric data to a file which is different from writting string data type
write() method writes only string type to a file so to write a numeric data type, first convert it
to string type using str()method
"""

# function to start the program
def main():

	# lets get some numeric data from the user so we can use in mathematic calculations later on
	# get user input
	height = float(input("Enter your height in centimeters: "))
	weight = float(input("Enter your weight in kilograms: "))

	# open a new file called 'numeric_type.txt' in 'w' access mode
	file_output = open("numeric_type.txt", 'w')

	# write the data to the file, but convert to string first using the str() method
	file_output.write(str(height) + '\n')
	file_output.write(str(weight) + '\n')

	# close the file
	file_output.close()

# call the main function
main()
