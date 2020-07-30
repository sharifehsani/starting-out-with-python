"""
- Author: Sharif Ehsani
- Date: July 2020
- www.gitbuh.com/ehsanis
- This program averages test scores. It asks the user for the number of students and the number of test scores per student
- and displays the average of tests per student.
"""




# main function to start the program

def main():
	print()
	print("This program averages test scores. It asks the user for the number of students and the number " + 
		"of test scores per student.")
	
	student_number = int(input("How many students' test would you like to calculate? "))
	test_number = int(input("How many test score per student do you have? "))

	# input validation for number of stduents and number of tests per student
	while (student_number <= 0 or test_number <= 0):
		print("Wrong input! number of students or number of tests must be a positive number greater than zero.")
		student_number = int(input("How many students' test would you like to calculate? "))
		test_number = int(input("How many test score per student do you have? "))

	# if number of students and number of tests >= zero call the calculate_average function and pass them as arguments
	calculate_average(student_number, test_number)



# function to calculate average
def calculate_average(student_number, test_number):

	for student in range(1, student_number + 1):
		print() 
		test_score = 0.0
		average = 0.0
		print("Student Number: ", student)
		print("--------------------------")

		for test in range(1, test_number + 1):

			print("Enter test number ", test,end='')
			score = float(input( ": "))
			test_score = test_score + score
			average = test_score / test_number
			
		print("Average for student number ", student, " is: ", average)

	

# call the main function
main()