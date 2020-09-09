"""
- Author: Sharif Ehsani
- Date: September 2020
- www.gitbuh.com/ehsanis

Algorithm workbench
3. Assume the lists numbers1 has 100 elements and numbers2 is an empty list. Write code that copies the values in numbers1 to numbers2.
"""

# main function to start the program
def main():

	# lets just have a list with 10 elements instead of 100 elements
	numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	# initialize an empty list variable
	numbers2 = []
	numbers3 = []

	# there are 2 ways we can copy elements of list one to another list
	# way 1: loop through the list element and append each element to the new list
	for num in numbers1:
		# append elements of numbers1 list to numbers2 list
		numbers2.append(num)

	# print numbers2 list
	print("Numbers2 list: ", numbers2)

	# another way is to concatinate an empty list with the first list
	numbers3 = numbers3 + numbers1

	print("Numbers3 list: ", numbers3)


# call the main function
main()