"""
- Author: Sharif Ehsani
- Date: December 2020
- https://github.com/sharifehsani

Algorithm Workbench
11. Assume the variable dct references a dictionary. Write code that pickles the dictionary
and saves it to a file named mydata.dat.
"""

# import pickle
import pickle


# function to write and save data
def write_and_save(friend, out_file):

	# in a dictonary save name, age and weight of people
	print("Enter the follwong info for your friends.")
	friend["Name"] = input("Name: ")
	friend["Phone"] = input("Age: ")
	friend["Weight"] = input("Weight: ")

	# write the dictionary into file
	pickle.dump(friend, out_file)


# main function to start
def main():

	# delcare a dictonary variable
	friend = {}

	# open a binary file for writting with 'wb' type
	out_file = open("mydata.dat", "wb")
	print("File is open for writting.")


	# get the user to fill the dictonary
	# counter variable to run the while loop
	more = 'y'
	while (more == 'y'):

		# call the the write_and_save method
		write_and_save(friend, out_file)

		# ask user if wants to add more
		more = input("Do you want to add more? (y/n): ")


	# close the data file
	out_file.close()
	print("File saved and closed.")


# cal the main function
main()
