"""
- Author: Sharif Ehsani
- Date: August 2020
- www.gitbuh.com/ehsanis

This program gets employee data from the user and
saves it as records in the employee.txt file.
"""

# main function to start the program
def main():
	# creat and open 'employees.txt' file in 'w' access mode
	file_out = open('employees.txt', 'w')

	# ask the user how many employees needed to be added
	number_of_emplyees = int(input("How many emplyees do you want to add: "))

	# creat a for loop to run as many times as the number of employees
	for count in range(1, number_of_emplyees + 1):
		print("Enter the information about emplyee #", count)
		# get emplyee's information from the user
		emp_name = input("Emplyee name: ")
		emp_id = input("Employee ID: ")
		emp_department = input('Emplyee department: ')

		# write the employee info to the file
		file_out.write(emp_name + '\n')
		file_out.write(emp_id + '\n')
		file_out.write(emp_department + '\n')
		# seperate the emplyees for readablity
		print()

	# close the file
	file_out.close()
	print("All records saved.")


# call the main function
main()
