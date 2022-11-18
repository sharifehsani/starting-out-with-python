"""
- Author: Sharif Ehsani
- Date: September 2020
- https://github.com/sharifehsani

Algorithm workbench
7. What will the following code print?
list1 = [40, 50, 60] list2 = [10, 20, 30] list3 = list1 + list2 print(list3)
"""

# main function to start the program
def main():

	#7. What will the following code print?
	# the statement in line 16 initializes a list variable and assigns 3 elements
	list1 = [40, 50, 60] 
	# the statement in line 18 initializes a list variable with 3 integer elements
	list2 = [10, 20, 30] 
	# the statement in line 20 concatinates the list1 with list2 and assigns to list3
	list3 = list1 + list2 
	# the statement in line 22 prints the elements of list3
	print(list3)	# prints: [40, 50, 60, 10, 20, 30]



# call the main function
main()
