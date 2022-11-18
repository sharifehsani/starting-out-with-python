"""
- Author: Sharif Ehsani
- Date: June 2020
- https://github.com/sharifehsani

8. Tip, Tax, and Total
Write a program that calculates the total amount of a meal purchased at a restaurant. The
program should ask the user to enter the charge for the food, and then calculate the amount
of a 15 percent tip and 7 percent sales tax. Display each of these amounts and the total.
"""

food_price = float(input("Enter the meal price: "))

tip = food_price * 0.15
tax = food_price * 0.07
total = food_price + tip + tax

print("Meal price: ", format(food_price, '.2f'))
print("Tip amount at 15 %:", format(tip, '.2f'))
print("Tax amount at 7 %:", format(tax, '.2f'))
print("Total: ", format(total, '.2f'))
