"""
- Author: Sharif Ehsani
- Date: August 2020
- www.gitbuh.com/ehsanis

Totaling the Values in a List
Assuming a list contains numeric values, to calculate the total of those values you use a loop with an 
accumulator variable. The loop steps through the list, adding the value of each element to the accumulator.
"""

# function to start the program
def main():

	# creat a list with 5 elements in it
	my_list = [6, 20, 10, 14, 9]

	# accumulator variable to hold total
	total = 0

	# in a loop step through list elments
	for element in my_list:
		# add each value (element) to the accumulator
		total = total + element

	# print the total
	print("The sum of all the values in the list =", total)



# call the main function
main()

