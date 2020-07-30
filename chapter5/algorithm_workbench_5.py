"""
- Author: Sharif Ehsani
- Date: July 2020
- www.gitbuh.com/ehsanis

5. Write a loop that calculates the total of the following series of numbers:
1/30 + 2/29 + 3/28 + … 30/1
"""

# main function to start the program
def main():
	print() 	# blanck line to seperate the program from the command line for readablity
	print('This program calculates the total of the following series of number 1/30 + 2/29 + 3/28 + … 30/1')

	# this can be accomplished by using nested loops as below
	"""
	product = 0
	for numerator in range(1, 31):
		for denominator in range(30, 1, -1):

			total = numerator / denominator
			product = product + total
			#print(numerator, " / ", denominator)
			print('product = ', numerator, "/", denominator, format(product,'.2f'))
			numerator = numerator + 1
			denominator = denominator - 1
	"""
	# This way is much simpler
	product = 0
	denominator = 30
	for numerator in range(1, 31):
		total = numerator / denominator 
		product = product + total
		
		print("product = ", numerator, " / ", denominator, ' = ', format(product, '.2f'))
		denominator = denominator -1



# call the main function
main()