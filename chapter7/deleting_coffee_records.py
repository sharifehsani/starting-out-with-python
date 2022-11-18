"""
- Author: Sharif Ehsani
- Date: August 2020
- https://github.com/sharifehsani

Deleting Records
Your last task is to write a program that Julie can use to delete records from the
coffee_records.txt file. Like the process of modifying a record, the process of deleting a record
from a sequential access file requires that you create a second temporary file. You copy all
of the original file’s records to the temporary file, except for the record that is to be deleted.
The temporary file then takes the place of the original file. You delete the original file and
rename the temporary file, giving it the name that the original file had on the computer’s
disk. 
Here is the general algorithm for your program:

Open the original file for input and create a temporary file for output.
Get the description of the record to be deleted.
Read the description field of the first record in the original file.
While the description is not empty:
Read the quantity field.
If this record’s description field does not match the description entered:
Write the record to the temporary file.
Read the next description field.
Close the original file and the temporary file.
Delete the original file.
Rename the temporary file, giving it the name of the original file.
"""

# imporst os module to remove and rename files
import os

# function to start the program
def main():

	# creat a boolean variable to use as a flag
	match_found = False

	# open the original file (coffee_records.txt) in 'r' access mode
	file_in = open('coffee_records.txt', 'r')

	# creat atemporary file named temporary.txt for output
	file_out = open('temporary_file.txt', 'w')

	# get the disription of the record to be deleted
	record_to_delet = input("Enter the disription / name of the record to be deleted: ")

	# read the first line (discription field of the record)
	description_field = file_in.readline()


	# in a loop read all the lines in the file
	while (description_field != ''):

		# read the quantity field of the record and convert it to float
		quantity_field = file_in.readline()
		#quantity_field = float(quantity_field)

		# strip the new line from the end of the line read
		
		description_field = description_field.rstrip('\n')

		# match the record with the records to be deleted
		# write everything else to the temporary file other than the match found
		if (record_to_delet != description_field):
			file_out.write(description_field + '\n')
			file_out.write(str(quantity_field))		# make sure to conveert floating point value to string

			# set the flag to be true
			match_found = True

		else:
			match_found = False
			print("Match found")


		# read the next line
		description_field = file_in.readline()



	# close both input and output files
	file_in.close()
	file_out.close()

	# delet the original file
	os.remove("coffee_records.txt")

	# rename the temporary file to original file
	os.rename('temporary_file.txt', 'coffee_records.txt')

	# print the result
	if match_found:
		print("record not found.")
			
	else:
		print("Record updated")


# call the main function
main()

