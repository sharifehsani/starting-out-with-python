import random		# import random module from the standard library
"""
- Author: Sharif Ehsani
- Date: July 2020
- www.gitbuh.com/ehsanis

2. Math Quiz
Write a program that gives simple math quizzes. The program should display two random
numbers that are to be added, such as:
247
+ 129
The program should allow the student to enter the answer. If the answer is correct, a message
of congratulations should be displayed. If the answer is incorrect, a message showing
the correct answer should be displayed.
"""

# function to start the program
def main():
	print()
	print("This program generates two random numbers and ask the user to add them and enter the answer \n"+ 
		"The program then tells the user of the answer was correct or incorrect.")

	# generate 2 random numbers
	first_number = random.randint(1, 1000)
	second_number = random.randint(1, 1000)
	# add the 2 numbers together
	sum = first_number + second_number

	# get the user to answer the math quiz
	print("What is ", first_number, " + ", second_number, "? ", end='')
	result = int(input(": "))

	# check if the answer is correct
	if (sum == result):
		print("congratulations!, your answer is correct.")

	else:
		print("Sorry -: your answer is incorrect, the right answer is ", sum)


# call the main function
main()
