"""
- Author: Sharif Ehsani
- Date: July 2020
- https://github.com/sharifehsani

- A running total is a sum of numbers that accumulates with each iteration of a loop.
- The variable used to keep the running total is called an accumulator.
"""

# main function to start the program
def main():
	print("This program calculates the total sale of a business weekly.")

	total = 0.0
	more = "y"
	while (more == 'y'):
		sale = float(input("Enter dayly sales: "))
		more = input('Is there more sales to add? enter "y" for yes and any other key for "no": ')
		total = total + sale

	print("Your total weekly sale is: $", format(total, '.2f'),sep='')


# call the main function
main()
