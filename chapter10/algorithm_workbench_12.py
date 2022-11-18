"""
- Author: Sharif Ehsani
- Date: December 2020
- https://github.com/sharifehsani

Algorithm Workbench
12. Write code that retrieves and unpickles the dictionary that you pickled in Algorithm
"""
# make sure to impor pickle
import pickle

# main function to start the program
def main():

	# open the binary file name mydata.dat in binary read format
	file_in = open("mydata.dat", "rb")

	# check for the end of file to end reading
	end_of_file = False

	while not end_of_file:
		# in a try and except cluase read the file
		try:
			friend = pickle.load(file_in)
			# call the display function to display the content of the file
			display_method(friend)

		except EOFError:
			end_of_file = True

	# close the file
	file_in.close()


# functio to display the content of the file
def display_method(friend):
	
	print("Name:", friend["Name"])
	print("Phone:", friend["Phone"])
	print("Weight:", friend["Weight"])
	print()



# call the main function
main()
