"""
- Author: Sharif Ehsani
- Date: June 2020
- www.gitbuh.com/ehsanis

2. Areas of Rectangles
The area of a rectangle is the rectangle’s length times its width. Write a program that asks
for the length and width of two rectangles. The program should tell the user which rectangle
has the greater area, or if the areas are the same.
"""

# function to start the program
def main():
	print()
	print("This program asks the user to entr the length and width of two rectangles, then tells the user which rectangle has greater area.")
	get_input()

# function to get input
def get_input():

	length_one = float(input("Enter the lenght of rectangle one: "))
	width_one = float(input("Enter the width of rectangle one: "))
	length_two = float(input("Enter the lenght of rectangle two: "))
	width_two = float(input("Enter the width of rectangle two: "))
	calculate_area(length_one, width_one, length_two, width_two)	

# function to calculate area
def calculate_area(length_one, width_one, length_two, width_two):
	area_one = length_one * width_one
	area_two = length_two * width_two

	if (area_one == area_two):
		print("The area of the both rectangles are the same.")
	elif (area_one > area_two):
		print("Rectangle one ",area_one, " is greater than rectangle two ", area_two)
	else:
		print("Rectangle two ",area_two, " is greater than rectangle one ", area_one)

# call the main function
main()