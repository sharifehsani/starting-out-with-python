"""
- Author: Sharif Ehsani
- Date: June 2020
- www.gitbuh.com/ehsanis

3. Mass and Weight
Scientists measure an object’s mass in kilograms and its weight in newtons. If you know the
amount of mass of an object in kilograms, you can calculate its weight in newtons with the
following formula:
weight = mass x 9.8
Write a program that asks the user to enter an object’s mass, and then calculates its weight.
If the object weighs more than 1,000 newtons, display a message indicating that it is too
heavy. If the object weighs less than 10 newtons, display a message indicating that it is too
light.
"""

# main function to start the rogram
def main():
	print("This program calcuates the weight of an object knowing the mass of it.")
	get_input()

# fnction to get user input
def get_input():
	mass = float(input("Enter an object’s mass in kilograms: "))
	calculate_weight(mass)

# function to calculate weight
def calculate_weight(mass):
	weight = mass * 9.8
	if (weight > 1000.0):
		print("This object is very heavy and its weight is: ", format(weight, '.2f'), " newtons")
	elif (weight < 10.0):
		print("This object is very light and its weight is: ", format(weight, '.2f'), " newtons")
	else:
		print("The weight of your object with the mass of ", mass, " kg is: ", format(weight, '.2f'), "newtons")

# call the main function
main()