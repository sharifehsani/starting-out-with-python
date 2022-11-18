"""
- Author: Sharif Ehsani
- Date: July 2020
- https://github.com/sharifehsani

4. Write a loop that asks the user to enter a number. The loop should iterate 10 times and
keep a running total of the numbers entered.
"""

# main function to start the program
def main():
	print() 	# blanck line to seperate the program from the command line for readablity
	print('This program asks the user to enter a number, the loop iterates 10 times and it keeps a running total '+
	'of the number entered ')
	# call the get_input function
	get_input()

# function to get input
def get_input():
	number = int(input("Enter a number: "))		# get an int number from the user
	# call the product() function and pass the number as parameter
	product(number)
	

# function to sum the product of the number
def product(number):
	product = 0		# running total
	for num in range(1, 11):		# remember that range() function includes 1, but does not include 11, goes up to 10
		product = product + number
		print("Product ", product)

# call the main function
main()
