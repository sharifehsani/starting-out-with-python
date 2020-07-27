"""
- Author: Sharif Ehsani
- Date: June 2020
- www.gitbuh.com/ehsanis

In the Spotlight:
Using the if Statement
Kathryn teaches a science class and her students are required to take three tests. She wants
to write a program that her students can use to calculate their average test score. She also
wants the program to congratulate the student enthusiastically if the average is greater than
95. Here is the algorithm in pseudocode:
Get the first test score
Get the second test score
Get the third test score
Calculate the average
Display the average
If the average is greater than 95:
Congratulate the user
"""

# main function to start the program
def main():
	intro_message()

# function to display intro messages
def intro_message():
	print("This program calculates average test score and congratulate students if the their score is higher than 95%")
	get_input()

# function to get user input
def get_input():
	tes_score_one = float(input("Enter your first test score: "))
	tes_score_two = float(input("Enter your second test score: "))
	tes_score_three = float(input("Enter your third test score: "))
	calculate_average(tes_score_one, tes_score_two, tes_score_three)

# function to calculate average
def calculate_average(score_one, score_two, score_three):
	total_score = score_one + score_two + score_three
	average_score = total_score / 3
	display_message(average_score)

# function to display message
def display_message(average_score):
	if (average_score > 95):
		print("Congratulation! you rocked it.")
	else:
		print("Sorry! your average is less than 95%.")



# call the main function
main()