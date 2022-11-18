"""
- Author: Sharif Ehsani
- Date: August 2020
- https://github.com/sharifehsani

Averaging the Values in a List
The first step in calculating the average of the values in a list is to get the total of the values. 
You saw how to do that with a loop in the preceding section. The second step is to divide the total by the 
number of elements in the list.
"""

# main function to start the program
def main():

	# creat a list with some values
	my_list = [3, 5, 19, 7, 2, 14]

	# initialize sum, average and number_of_elements variables
	sum = 0
	average = 0.0
	number_of_elements = len(my_list)

	# in a for loop step through each elements of the list
	for each_element in my_list:
		# add the values and assign to sum
		sum += each_element


	# calculate the average
	average = sum / number_of_elements

	# print the result
	print("number of elments in the list =", number_of_elements)
	print("The sum of all the values in the list =", sum)
	print("The average of all the elements of the list =", format(average, '.2f'))

# call the main function
main()
