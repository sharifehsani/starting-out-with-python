"""
- Author: Sharif Ehsani
- Date: June 2020
- https://github.com/sharifehsani

In the Spotlight:
Defining and Calling Functions
Professional Appliance Service, Inc. offers maintenance and repair services for household
appliances. The owner wants to give each of the company’s service technicians a small
handheld computer that displays step-by-step instructions for many of the repairs that
they perform. To see how this might work, the owner has asked you to develop a program
that displays the following instructions for disassembling an Acme laundry dryer:
Step 1: Unplug the dryer and move it away from the wall.
Step 2: Remove the six screws from the back of the dryer.
Step 3: Remove the dryer’s back panel.
Step 4: Pull the top of the dryer straight up.
"""
def main():
	print_message()
	print('Thanks for using this guide "STAY SAFE!!!"')

def print_message():
	print("This is a guide on how to desassemble an ACME laundry dryer.")
	print()
	input('Press "Enter" to start: ')
	print()
	print("There are 4 steps in the process: ")
	print()
	input('Press "Enter" to see step one: ')
	step_one()

def step_one():
	print("Step 1: Unplug the dryer and move it away from the wall.")
	print()
	input('Press "Enter" to see step two: ')
	step_two()

def step_two():
	print("Step 2: Remove the six screws from the back of the dryer.")
	print()
	input('Press "Enter" to see step three: ')
	step_three()

def step_three():
	print("Step 3: Remove the back panel from the dryer.")
	print()
	input('Press "Enter" to see step four: ')
	step_four()

def step_four():
	print("Step 4: Pull the top of the dryer straight up.")
	print()
	input('Press "Enter" to end: ')

main()
