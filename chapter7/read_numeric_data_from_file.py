"""
- Author: Sharif Ehsani
- Date: August 2020
- https://github.com/sharifehsani

This program reads numeric data type from a file and uses it in calculations
this program will convert the height (cm) and weight (kg) to pounds and feet
"""

# function to start the program
def main():

	# first open the file in 'r' read access mode
	file_input = open('numeric_type.txt', 'r')

	# read the data line by line since we know there are only 2 lines of data
	# since write() method only writes string type we have to convert it to float now to use it in calculations
	# NOTE: float() and int() mehtods IGNORE the '\n' new line at the end of the line
	your_height = float(file_input.readline())
	your_weight = float(file_input.readline())

	# now close the file since the data is read
	file_input.close()

	
	# the numeric data that was converted from string to float can now be used for calculations
	# here the height and weight are converted to feet and pounds
	height_in_feet = your_height / 30.48
	weight_in_pound = your_weight * 2.205



	print("your_height in centimeters is: ", format(your_height,'.2f'))
	print('your_weight in kilograms is: ', format(your_weight, '.2f'))

	print("your_height in feet is: ", format(height_in_feet,'.2f'))
	print('your_weight in pounds is: ', format(weight_in_pound, '.2f'))


# call the main function
main()
