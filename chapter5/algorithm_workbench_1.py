"""
- Author: Sharif Ehsani
- Date: July 2020
- www.gitbuh.com/ehsanis

1. Write a while loop that lets the user enter a number. The number should be multiplied
by 10, and the result assigned to a variable named product. The loop should iterate as
long as product is less than 100.
"""

# main function to start the program
def main():
	print()		# blanck line to seperate the program from the command line for readablity
	print("This program gets user input (a number), then the number is multiplied by 10 as long as the product "+
		"is less than 100")

	# call get_input() function
	get_input()


# function to get user input
def get_input():
	number = int(input("Enter a positive nubmer: "))
	# validate the input to make sure a positive number is entered
	while (number <= 0):
		print("ERROR! the number should be greater than zero.")
		number = int(input("Enter a positive nubmer: "))

	# call multiply_by_ten() function and pass number as parameter
	multiply_by_ten(number)

# function to multiply the number by ten
def multiply_by_ten(number):
	product = 0
	print("The number =\t", number)
	while (product < 100):		# exit the loop when the product is greater than or equal to 100
		product = product + (number * 10)
		print(product)

	print("The product =  ",  product)	

# call the main function
main()