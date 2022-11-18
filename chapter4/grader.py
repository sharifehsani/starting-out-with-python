"""
- Author: Sharif Ehsani
- Date: June 2020
- https://github.com/sharifehsani

In the Spotlight:
Multiple Nested Decision Structures
Dr. Suarez teaches a literature class and uses the following 10 point grading scale for all of
his exams:
Test Score Grade
90 and above A
80–89 B
70–79 C
60–69 D
Below 60 F
He has asked you to write a program that will allow a student to enter a test score and then
display the grade for that score. Here is the algorithm that you will use:
1. Ask the user to enter a test score.
2. Determine the grade in the following manner:
If the score is greater than or equal to 90, then the grade is A.
Else, if the score is greater than or equal to 80, then the grade is B.
Else, if the score is greater than or equal to 70, then the grade is C.
Else, if the score is greater than or equal to 60, then the grade is D.
Else, the grade is F.
You decide that the process of determining the grade will require several nested decision
structures, as shown in Figure 4-17. Program 4-6 shows the code for the program. The code
for the nested decision structures is in lines 15 through 27.
"""
# function to start the program
GRADE = ''
def main():
	print("This 10 point grading scale program determines your test grading letter.")
	get_input()

# function to get user input
def get_input():
	test_score = float(input("Enter your test score: "))
	grader(test_score)

# function to calculate grades
def grader(test_score):
	if (test_score >= 90.0):
		GRADE = 'A'
	elif (test_score >= 80 and test_score < 90):
		GRADE = 'B'
	elif (test_score >= 70 and test_score < 80):
		GRADE = 'C'
	elif (test_score >= 60 and test_score < 70):
		GRADE = 'D'
	else:
		GRADE = 'F'
	display_message(GRADE)

def display_message(GRADE):
	print("Your grade is: ", GRADE)

# call the main function
main()
