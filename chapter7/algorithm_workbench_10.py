"""
- Author: Sharif Ehsani
- Date: August 2020
- https://github.com/sharifehsani

Algorithm Workbench
10. What will the following code display?
The following code will display the print statements on line 32 and 35
"""

# function to start the program
def main():
	# the try suite will raise a ValueError exception since the float()method will not be able
	# to convert the string 'abc123' to floating point value
	try:
		# 'abc123' is passed as an argument to float() method and assigned to variable x
		x = float('abc123')
		# this statement is ignored
		print(x)
	# this except clause handles input output error, so since the exception raised as value error,
	# this block of code is ignored
	except IOError:
		print('This code caused an IOError.')

	# this except clause handles ZeroDivisionErro and so this block is also ignored
	except ZeroDivisionError:
		print('This code caused a ZeroDivisionError.')

	# this except clause handles all kinds of exceptions, so this block will be executed
	except:
		print('An error happened.')

	# this statement will also be executed at the end
	print('The end.')

# call the main function
main()
