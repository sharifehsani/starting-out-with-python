"""
- Author: Sharif Ehsani
- Date: August 2020
- https://github.com/sharifehsani

Modifying Records
Julie is very happy with the programs that you have written so far. Your next job is to write
a program that she can use to modify the quantity field in an existing record. This will
allow her to keep the records up to date as coffee is sold or more coffee of an existing type
is added to inventory.
To modify a record in a sequential file, you must create a second temporary file. You copy
all of the original file’s records to the temporary file, but when you get to the record that is
to be modified, you do not write its old contents to the temporary file. Instead, you write
its new modified values to the temporary file. Then, you finish copying any remaining
records from the original file to the temporary file.
The temporary file then takes the place of the original file. You delete the original file and
rename the temporary file, giving it the name that the original file had on the computer’s
disk. 

Here is the general algorithm for your program:

Open the original file for input and create a temporary file for output.
Get the description of the record to be modified and the new value for the quantity.
Read the first description field from the original file.
While the description field is not empty:
Read the quantity field.
If this record’s description field matches the description entered:
Write the new data to the temporary file.
Else:
Write the existing record to the temporary file.
Read the next description field.
Close the original file and the temporary file.
Delete the original file.
Rename the temporary file, giving it the name of the original file.

"""
# import os module as needed for the removing and renaming file
import os	

# main function to start the program
def main():
	
	# use a boolean variable to use as flag
	match_found = False

	# open the 'coffee_records.txt' file as 'r' access mode
	file_in = open("coffee_records.txt", "r")

	# creat a temporary file for output in 'w' access mode
	temp_file = open("temporary_file.txt", "w")

	# get the discription of the the recor to be modified and the new value for the quantity
	record_to_modify = input("Enter the discription/ name of the record to be modified: ")

	# new quantity value variable
	new_quantity_value = 0.0

	# read the first line (description) field from the file
	discription_field = file_in.readline()

	# creat a loop with the condition to continue as long as there is more line to be read
	while (discription_field != ''):

		# now read the second field(quantity) and convert the string to float and no need to strip the new
		# line since float() method ignores the new line
		quantity_field = file_in.readline()
		#quantity_field = float(quantity_field)

		# strip the new line from the discription field
		# note the 
		discription_field = discription_field.rstrip('\n')

		# see if the discription matches
		if (record_to_modify == discription_field):
			
			# if the record to modify mathes the record discription write it to the temprary file
			temp_file.write(discription_field + '\n')

			# get the new quantity value from the user
			new_quantity_value = float(input("Enter the quantity amount: "))

			# write the new value to temp file
			temp_file.write(str(new_quantity_value) + '\n')
			match_found = True

		# if the record to modify does not match the coffee recods write the whole thing to the temp file
		else:
			temp_file.write(discription_field + '\n')
			# convert the float type to string first
			# do not add the new line at the end of this field because it will add a new line at
			# the end of each quantity line
			temp_file.write(str(quantity_field))	


		# read the next line
		discription_field = file_in.readline() 

	# close the original and temporary files
	file_in.close()
	temp_file.close()

	# delet the original file
	os.remove("coffee_records.txt")

	# rename the temporary file to original file
	os.rename("temporary_file.txt", "coffee_records.txt")

	# print info about what happened
	if (match_found == True):
		print("Record updated.")
	else:
		print("Match not found.")


# call the main function
main()
