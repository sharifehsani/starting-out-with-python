"""
- Author: Sharif Ehsani
- Date: August 2020
- https://github.com/sharifehsani

This program reads employee data from the file 'emplyees.txt' created earlier and displays
"""

# main function to start the program
def main():
	# open the file in 'r' access mode
	file_in = open('employees.txt', 'r')

	# in a while loop read lines until there is no more lines to be read. While loop works best since we know how many
	# lines are there and print the data

	# read the first line = name
	name = file_in.readline()

	while (name != ''):
		# read emplyee id
		emp_id = file_in.readline()

		# read department
		emp_department = file_in.readline()

		# remove the new line from the end of each line
		name = name.rstrip('\n')
		emp_id = emp_id.rstrip('\n')
		emp_department = emp_department.rstrip('\n')

		# print the above data
		print("Employee name: ", name)
		print("Emplyee ID: ", emp_id)
		print("emp_department: ", emp_department)
		print()

		# read the emplyee name again
		name = file_in.readline()

	# close the file
	file_in.close()

# call the main function
main()
