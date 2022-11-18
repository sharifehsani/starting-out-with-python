"""
- Author: Sharif Ehsani
- Date: June 2020
- https://github.com/sharifehsani

1. Kilometer Converter
Write a program that asks the user to enter a distance in kilometers, and then converts that
distance to miles. The conversion formula is as follows:
Miles = Kilometers * 0.6214
"""

def main():
	km = float(input("Enter a distance in kilometers: "))
	print()
	miles = convert_km_to_miles(km)
	print(km, " kilometers = ", format(miles,'.4f'), ' miles')

def convert_km_to_miles(km):
	miles = km * 0.6214
	return miles

main()
