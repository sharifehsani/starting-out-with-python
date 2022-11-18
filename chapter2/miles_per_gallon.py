"""
- Author: Sharif Ehsani
- Date: June 2020
- https://github.com/sharifehsani

7. Miles-per-Gallon
A car’s miles-per-gallon (MPG) can be calculated with the following formula:
Write a program that asks the user for the number of miles driven and the gallons of gas
used. It should calculate the car’s MPG and display the result.
"""

number_of_miles = float(input("Enter number of miles driven: "))
gallon_of_gas_used = float(input("Enter gallons of gas used: "))
mpg = number_of_miles / gallon_of_gas_used		#mpg = miles/gallon
print("miles per gallon = ", mpg)
