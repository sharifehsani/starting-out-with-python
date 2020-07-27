"""
- Author: Sharif Ehsani
- Date: June 2020
- www.gitbuh.com/ehsanis

7. Calories from Fat and Carbohydrates
A nutritionist who works for a fitness club helps members by evaluating their diets. As part
of her evaluation, she asks members for the number of fat grams and carbohydrate grams
that they consumed in a day. Then, she calculates the number of calories that result from
the fat, using the following formula:
calories from fat = fat grams x 9
Next, she calculates the number of calories that result from the carbohydrates, using the
following formula:
calories from carbs = carb grams x 4
The nutritionist asks you to write a program that will make these calculations.
"""

def main():
	intro_message()


# Funtion to display message
def intro_message():
	print()
	print('This program calculates the number of calories that result from the fat grams and carbohydrates grams\nyou are using daily by evaluating your diet.')
	get_user_input()

# function for geting user input
def get_user_input():

	fat = float(input(('Please enter the number of fat grams you have consumed today: ')))
	carb = float(input(('Please enter the number of carbohydrates you have consumed today: ')))
	calculate_calories_from_fat(fat)
	calcuate_calories_from_carb(carb)

# Function to calculate calories form fat
def calculate_calories_from_fat(fat):
	cal_from_fat = fat * 9
	print('Number of calories that result from the daily fat use = ', format(cal_from_fat, '.2f'), 'calories')

# Function to calculate calories form carbohydrates
def calcuate_calories_from_carb(carb):
	cal_from_carb = carb * 4
	print('Number of calories that result from the daily carbohydrates use = ', format(cal_from_carb, '.2f'), 'calories')


main()
