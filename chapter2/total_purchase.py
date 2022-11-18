"""
- Author: Sharif Ehsani
- Date: June 2020
- https://github.com/sharifehsani

4. Total Purchase
A customer in a store is purchasing five items. Write a program that asks for the price of
each item, and then displays the subtotal of the sale, the amount of sales tax, and the total.
Assume the sales tax is 6 percent.
"""
item_one = float(input("Enter the price of item # 1: "))
item_two = float(input("Enter the price of item # 2: "))
item_three = float(input("Enter the price of item # 3: "))
item_four = float(input("Enter the price of item # 4: "))
item_five = float(input("Enter the price of item # 5: "))
subtotal = item_one + item_two + item_three + item_four + item_five
tax = subtotal * 0.06
total = subtotal + tax
print("Subtotal: ", subtotal)
print("Tax: ", tax)
print("Grand Total: ", total)
