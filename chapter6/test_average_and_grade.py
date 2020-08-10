"""
- Author: Sharif Ehsani
- Date: July 2020
- www.gitbuh.com/ehsanis

6. Test Average and Grade
Write a program that asks the user to enter five test scores. The program should display a letter
grade for each score and the average test score. Write the following functions in the program:
• calc_average—This function should accept five test scores as arguments and return
the average of the scores.
• determine_grade—This function should accept a test score as an argument and
return a letter grade for the score, based on the following grading scale:
Score Letter Grade
90–100 A
80–89 B
70–79 C
60–69 D
Below 60 F
"""

# function to start the program
def main():
	print()
	print("This program converts test scores to letter grade.")

	# call get_input function
	one, two, three, four, five = get_input()


	# once you get the input call calc_average_this function and pass the test scores as parameters and assign
	# the returned value to test_average
	test_average = calc_average_this(one, two, three, four, five)

	# call the determine_grade and pass the test average as a parameter and assign the result to result variable
	result = determine_grade(test_average)
	

	# display the result
	print('Your average test score is: ', test_average, 'and your letter grade is: ', result)

# function to get user input
def get_input():
	# get user input for all the 5 test
	score_one = float(input("Enter the score for test number 1: "))
	score_two = float(input("Enter the score for test number 2: "))
	score_three = float(input("Enter the score for test number 3: "))
	score_four = float(input("Enter the score for test number 4: "))
	score_five = float(input("Enter the score for test number 5: "))
	# return the values
	return score_one, score_two, score_three, score_four, score_five
	# end of function


# function to determine grade
def calc_average_this(one, two, three, four, five):
	# calculate the average of all 5 tests
	average = (one + two + three + four + five) / 5
	# return the result
	return average
	# end of function


# function to determine letter grade
def determine_grade(test_average):
	# determine letter_grade
	letter_grade = ''
	if (test_average >= 90 and test_average <= 100):
		letter_grade = 'A'
	elif (test_average >= 80 and test_average < 90):
		letter_grade = 'B'
	elif (test_average >= 70 and test_average < 80):
		letter_grade = 'C'
	elif (test_average >= 60 and test_average < 70):
		letter_grade = 'B'
	else:
		letter_grade = 'F'

	# return the letter grade
	return letter_grade
	# 3 end of function


# call the main function
main()

