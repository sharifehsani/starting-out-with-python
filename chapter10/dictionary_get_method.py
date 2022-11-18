"""
- Author: Sharif Ehsani
- Date: December 2020
- https://github.com/sharifehsani

dictonary methods
"""

# main function to start the program
def main():

	# declare a new dictonary variable with 5 keys and 5 values
	friends_phone_numbers = {"Sharif": "403503", "Bani": "403510", "Jack": "403511", "Naz": "403211" }
	print("This is the dictionary:")
	print(friends_phone_numbers)

	print("In a loop lets get a value of a key.")
	more = 'y'
	while more == 'y':
		get_key = input("Enter a key to get from dictionary using get method(): ")
		value = friends_phone_numbers.get(get_key, "The value does not exist.")
		print("This is the value found: ", value)
		more = input("Do you want to continue? y = yes, n = no: ")

	print("We are done.") 

# call the main function
main()
