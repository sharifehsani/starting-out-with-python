
"""
- Author: Sharif Ehsani
- Date: August 2020
- www.gitbuh.com/ehsanis

this program reads the content of an existing file named 'student_info.txt' with 'r' mode access and strips the new line
as we saw in the previous program 'read_from_a_file.py' when we printed the data read from the file it printed the new lines
as well so in this program we remove those new lines using rstrip() function 
"""

# function to start the program
def main():

	# open the file
	file_input = open('student_info.txt', 'r')

	# readd the lines one by one. We know there are 6 lines
	first_name = file_input.readline()
	last_name = file_input.readline()
	date_of_birth = file_input.readline()
	student_id = file_input.readline()
	faculty = file_input.readline()
	major = file_input.readline()

	# strip or remove the new line from the end of each line using rstrip() method
	first_name = first_name.rstrip('\n')
	last_name = last_name.rstrip('\n')
	date_of_birth = date_of_birth.rstrip('\n')
	student_id = student_id.rstrip('\n')
	faculty = faculty.rstrip('\n')
	major = major.rstrip('\n')


	# print the data read and the new line removed
	print()
	print("The following info was read from the file.")
	print("First name: ", first_name)
	print("last name: ", last_name)
	print("date of birth: ", date_of_birth)
	print("student_id: ", student_id)
	print("faculty: ", faculty)
	print("major: ", major)

# call the main function
main()