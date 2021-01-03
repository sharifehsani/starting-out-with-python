"""
- Author: Sharif Ehsani
- Date: December 2020
- www.gitbuh.com/ehsanis

Algorithm Workbench
10. Assume each of the variables set1 and set2 references a set. Write code that creates
another set containing the elements that are not shared by set1 and set2 and assigns
the resulting set to the variable set3.
"""

# main function to start
def main():

	# declare set variables and populate with some elements in common
	set1 = set(["Sharif", "Bani", "Naz", "Pet"])
	set2 = set(["Sharif", "Bani", "Naz", "Pet", "Dog"])
	# take the symmetric difference of both sets (element that is not shared in both)
	set3 = set1.symmetric_difference(set2)

	# display the result
	print("set1:", set1)
	print("set2:", set2)
	print("set3:", set3)


# call the main function
main()