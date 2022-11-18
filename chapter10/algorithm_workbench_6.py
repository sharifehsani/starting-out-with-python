"""
- Author: Sharif Ehsani
- Date: December 2020
- https://github.com/sharifehsani

Algorithm Workbench
6. Assume each of the variables set1 and set2 references a set. Write code that creates
another set containing all the elements of set1 and set2 and assigns the resulting set
to the variable set3.
"""

# main functoin to start the program
def main():
	# declare set1 and set2 and populate the sets
	set1 = set([1,2,3])
	set2 = set([4,5,6])
	# take the union of the two sets
	set3 = set1.union(set2)
	# display the result
	print("set1 =", set1)
	print("set2 =", set2)
	print("set3 =", set3)


# call the main function
main()
