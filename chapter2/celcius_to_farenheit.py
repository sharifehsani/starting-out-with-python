"""
- Author: Sharif Ehsani
- Date: June 2020
- https://github.com/sharifehsani

9. Celsius to Fahrenheit Temperature Converter
Write a program that converts Celsius temperatures to Fahrenheit temperatures. The formula
is as follows:
The program should ask the user to enter a temperature in Celsius, and then display the
temperature converted to Fahrenheit.
"""

temp_in_cel = int(input("Enter temperature in Celsius: "))
print(temp_in_cel, " degree Celsius equals to: ", ((temp_in_cel * 9/5) + 32), " degree fahrenheit.")
