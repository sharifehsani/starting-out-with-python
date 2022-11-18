"""
- Author: Sharif Ehsani
- Date: December 2020
- https://github.com/sharifehsani

Algorithm Workbench
7. Assume each of the variables set1 and set2 references a set. Write code that creates
another set containing only the elements that are found in both set1 and set2 and
assigns the resulting set to the variable set3.
"""

# main function to start the program
def main():

	 # creat 2 sets with some values
	 set1 = set([1,2,3,4])
	 set2 = set([2,3,5,6])

	 # fidn the common elements
	 set3 = set1.intersection(set2)

	 print("set1:", set1)
	 print("set2:", set2)
	 print("intersection of both sets:", set3)

# call the main function
main()
