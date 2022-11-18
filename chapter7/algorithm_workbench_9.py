"""
- Author: Sharif Ehsani
- Date: August 2020
- https://github.com/sharifehsani

Algorithm Workbench
9. What will the following code display?
The following code will display the print statements on line 27 and 29


"""
# function to start the program
def main():

	# the try suite raises an exception 
	try:
		# the float() method will not be able to covert the ('abc123') to float so it is a ValuError
		x = float('abc123')
		# this statement is ignored
		print('The conversion is complete.')
	# this statement handles file input output error, so this block is ignored
	except IOError:
		print('This code caused an IOError.')
	# this except clause handles value error, and since the try suite raised a ValueError exception
	# this block of code will run and print the print statment on line 27
	except ValueError:
		print('This code caused a ValueError.')
	# this is the last statment that will be executed.
	print('The end.')


# call the main function
main()
