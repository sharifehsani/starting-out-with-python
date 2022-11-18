"""
- Author: Sharif Ehsani
- Date: June 2020
- https://github.com/sharifehsani

9. Shipping Charges
The Fast Freight Shipping Company charges the following rates:
Weight of Package Rate per Pound
2 pounds or less $1.10
Over 2 pounds but not more than 6 pounds $2.20
Over 6 pounds but not more than 10 pounds $3.70
Over 10 pounds $3.80
Write a program that asks the user to enter the weight of a package and then displays the
shipping charges.
"""
SHIPPING_RATE = 0.0
SHIPPING_CHARGE = 0.0

# function to start the program
def main():
	print()
	print("This program calculates shipping charges for packages bassed on their weight (per pound)")
	get_input_display_message()

# function to get user input
def get_input_display_message():
	weight_of_package = float(input("Enter the weight of the package: "))
	total_shipping_charge = calculate_shipping_charge(weight_of_package)

	print("The shipping charges for ", format(weight_of_package,'.2f'), " pounds of package is $", format(total_shipping_charge,'.2f'), sep='')

# function to calculate shipping charge
def calculate_shipping_charge(weight_of_package):
	if (weight_of_package <= 2.0):
		SHIPPING_RATE = 1.10
		SHIPPING_CHARGE = weight_of_package * SHIPPING_RATE
		

	elif (weight_of_package > 2.0 and weight_of_package <= 6.0):
		SHIPPING_RATE = 2.20
		SHIPPING_CHARGE = weight_of_package * SHIPPING_RATE
		

	elif (weight_of_package > 6.0 and weight_of_package <= 10.0):
		SHIPPING_RATE = 3.70
		SHIPPING_CHARGE = weight_of_package * SHIPPING_RATE
		

	else:
		SHIPPING_RATE = 3.80
		SHIPPING_CHARGE = weight_of_package * SHIPPING_RATE
		
	return SHIPPING_CHARGE


# call the main function
main()
