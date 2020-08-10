"""
- Author: Sharif Ehsani
- Date: July 2020
- www.gitbuh.com/ehsanis

3. A program contains the following function definition:
def cube(num):
return num * num * num
Write a statement that passes the value 4 to this function and assigns its return value
to the variable result.

"""

# function to start the program
def main():
	print()
	print("This program gets an int from the user and cubes it.")
	# get the num value (an integer) from the user
	num = int(input("Enter an integer value: "))

	# call the cube function() and pass num as parameter when it returnes assign to the variable result
	result = cube(num)

	# print the result to the console
	print("The cube of ", num, " is: ", result)


# function to cube the num value
def cube(num):
	return num * num * num


# call the main function
main()