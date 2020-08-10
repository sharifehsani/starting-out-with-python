import random			# import random module from the standard library


"""
- Author: Sharif Ehsani
- Date: July 2020
- www.gitbuh.com/ehsanis

Algorithm Workbench
1. Write a statement that generates a random number in the range of 1 through 100 and
assigns it to a variable named rand.
"""

# function to start the program
def main():
	print()
	print("This program generates random number in the range of 1 through 100.")

	rand = random.randint(1,100)

	print("The random number generated in the range of 1 to 100 is: ", rand)



# call the main function
main()