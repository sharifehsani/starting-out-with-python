"""
- Author: Sharif Ehsani
- Date: December 2020
- https://github.com/sharifehsani

dictonary methods
"""

# main method to start the program
def main():

	# declare a dictionary method with some keys and values
	friends_que_number = {'Sharif':1, "Bani": 2, "Jack": 3, "Naz": 4, "Eli": 5 }

	print("Here is the dictionary befor popitem.", friends_que_number)

	print("The popitem method returns the last key-value pair, and it removes that key-value")
	print("format: dictionary.popitem()")

	key, value = friends_que_number.popitem()
	print("The follwong key =",key, "and value =", value, "was removed from the dictionary.")

	print("Here is the dictionary after the popitem.", friends_que_number)

# call the main method
main()
