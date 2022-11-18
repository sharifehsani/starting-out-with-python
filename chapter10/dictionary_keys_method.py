"""
- Author: Sharif Ehsani
- Date: December 2020
- https://github.com/sharifehsani

dictonary methods
"""

# main method to start the program
def main():

	# declare a dictionary method with some keys and values
	friends_phone_numbers = {"Sharif": "403503", "Bani": "403510", "Jack": "403511", "Naz": "403211" }

	print("The key method returns all of a dictionary’s keys as a dictionary view.")
	for key in friends_phone_numbers.keys():
		print(key)


# call the main method
main()
