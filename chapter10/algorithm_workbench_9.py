"""
- Author: Sharif Ehsani
- Date: December 2020
- www.gitbuh.com/ehsanis

Algorithm Workbench
9. Assume each of the variables set1 and set2 references a set. Write code that creates
another set containing the elements that appear in set2 but not in set1 and assigns the
resulting set to the variable set3.
"""

# main function to start
def main():

	# declare set variables with some elements in them
	set1 = set([1,2,3,4,5])
	set2 = set([6,7,8,9,10])

	# take the set2 - set1
	set3 = set2.difference(set1)

	# display the sets
	print("set1:", set1)
	print("set2:", set2)
	print("set3:", set3)


# call the main function
main()