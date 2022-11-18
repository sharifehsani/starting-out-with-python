"""
- Author: Sharif Ehsani
- Date: July 2020
- https://github.com/sharifehsani

2. Calories Burned
Running on a particular treadmill you burn 3.9 calories per minute. Write a program
that uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30
minutes.
"""

# main function to start the program
def main():
	# display the intro message about the program
	print('This program calculates the number of calories you burn after 10, 15, 20, 25, and 30 minutes on running on a treadmill.')
	print('Running on a particular treadmill you burn 3.9 calories per minutes.')

	# assign number 10 to the counter since it starts from 10 minutes
	minutes = 10
	calories_per_minute = 3.9			# every minute you burn 3.9 calories
	for number in range(5):
		total_calories = minutes * calories_per_minute
		print("You burn ", total_calories, ' calories every ', minutes, ' minutes.')
		minutes = minutes + 5			# increament counter by 5 at each iteration


# call the main function
main()



