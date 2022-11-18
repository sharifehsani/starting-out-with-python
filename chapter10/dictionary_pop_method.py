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

	print("The pop method returns the value associated with a specified key\
	 	and removes that key pop value pair from the dictionary.")
	print("This is the dictonary before pop.", friends_phone_numbers.items())
	more = 'y'
	while (more == 'y'):
		pop_me = input("Enter a key to pop from the dictonary: ")
		friends_phone_numbers.pop(pop_me)
		more = input("Do you want to continue? 'y' = yes, 'n' = no:")
	print("We are done and here is the new dictionary after pop.", friends_phone_numbers)



# call the main method
main()
