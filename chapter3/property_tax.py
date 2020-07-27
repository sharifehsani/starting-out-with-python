"""
- Author: Sharif Ehsani
- Date: June 2020
- www.gitbuh.com/ehsanis

5. Property Tax
A county collects property taxes on the assessment value of property, which is 60 percent
of the property’s actual value. For example, if an acre of land is valued at $10,000,
its assessment value is $6,000. The property tax is then 64¢ for each $100 of the assessment
value. The tax for the acre assessed at $6,000 will be $38.40. Write a program that
asks for the actual value of a piece of property and displays the assessment value and
property tax.
"""

# function to start the program
def main():
	display_message()

# function to display message
def display_message():
	print("This program calculates the assessment value and property tax on the assessment value of your property.")
	get_input() # call get_input fucntion

# function to get user input
def get_input():
	property_value = float(input("Please enter the actual value of the property:"))

	# call calculate_assessment_value function and pass property_value as parameter
	calculate_assessment_value(property_value)

# function to calculate assement value
def calculate_assessment_value(property_value):
	assessment_value = 0.6 * property_value
	print("The assessment value of your property is: $", format(assessment_value, '.2f'))

	# call the calculate_tax function and pass assessment_value as parameter
	calculae_tax(assessment_value)
	

# function calcuate tax
def calculae_tax(assessment_value):
	property_tax = 0.64 * (assessment_value / 100)
	print("Property tax on the assessment value of your property is: $", format(property_tax, '.2f'))

# call the main function
main()