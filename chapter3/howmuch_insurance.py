"""
- Author: Sharif Ehsani
- Date: June 2020
- https://github.com/sharifehsani

3. How Much Insurance?
Many financial experts advise that property owners should insure their homes or buildings
for at least 80 percent of the amount it would cost to replace the structure. Write a
program that asks the user to enter the replacement cost of a building and then displays
the minimum amount of insurance he or she should buy for the property.
"""


def main():
	display_message()
	

def display_message():
	print("Hi, this program tells you the minimum amount of insurance you need to replace your property.")
	print()
	insurance = get_input()
	print("You need at least $",insurance, " coverage to replace your property")

def get_input():
	building_cost = float(input("Enter your property cost: "))
	min_ins = calculate_insurance(building_cost)
	return min_ins


def calculate_insurance(building_cost):
	minimum_insurance = building_cost * 0.8
	return minimum_insurance


main()
