"""
- Author: Sharif Ehsani
- Date: December 2020
- https://github.com/sharifehsani

Algorithm Workbench
8. Assume each of the variables set1 and set2 references a set. Write code that creates
another set containing the elements that appear in set1 but not in set2 and assigns the
resulting set to the variable set3.
"""

# main function to start
def main():

	# declare two set variables with some elements in them with some common elements
	set1 = set([1,2,5,8,10,20])
	set2 = set([2,3,6,12,15])

	# find the difference of set1 and set2
	set3 = set1.difference(set2)

	# display the result
	print("set1:", set1)
	print("set2:", set2)
	print("set3:", set3)



# call the main function
main()
