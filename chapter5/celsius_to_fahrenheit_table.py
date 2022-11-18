"""
- Author: Sharif Ehsani
- Date: July 2020
- https://github.com/sharifehsani

6. Celsius to Fahrenheit Table
Write a program that displays a table of the Celsius temperatures 0 through 20 and their
Fahrenheit equivalents. The formula for converting a temperature from Celsius to
Fahrenheit is
F = (9/5) * C + 32
where F is the Fahrenheit temperature and C is the Celsius temperature. Your program
must use a loop to display the table.
"""


# main function to start the program
def main():
	# display the program discription
	print("This program calculates Celsius temperature to its Fahrenheit equivalents from 0 - 20. ")
	print()
	print("Degree Celsius \t \tDegree Fahrenheit")
	print("-------------------------------------------")
	for temp in range(21):
		f = ((9/5) * temp) + 32
		print(temp, "degree Celsius = ", format(f,'.2f'), "degree Fahrenheit.")


# call the main function
main()
