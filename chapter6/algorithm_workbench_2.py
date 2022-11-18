"""
- Author: Sharif Ehsani
- Date: July 2020
- https://github.com/sharifehsani

2. The following statement calls a function named half, which returns a value that is half
that of the argument. (Assume the number variable references a float value.) Write
code for the function.
result = half(number)
"""

# function to start the program
def main():
	print()
	print("This program tests a function called half(number) and the function returns half that of the argument.")
	# get user input
	number = float(input("Enter a number: "))
	# call the half function
	result = half(number)
	# print the returned value
	print("Half of ", format(number, '.1f'), " is ", format(result, '.1f'))



# function to half the parameter
def half(num):
	# devide the num value by 2 (half it)
	half_the_number = num / 2
	# return the halfed number to the caller
	return half_the_number

	# end of the function

# call the main function
main()
