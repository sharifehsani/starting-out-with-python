"""
- Author: Sharif Ehsani
- Date: June 2020
- www.gitbuh.com/ehsanis
"""
# This program calculates sale price for sale items

original_price = float(input("Please enter the original price: "))
discount = float(input("Enter the discount: "))
percentage = discount/ 100
discount_price = original_price - (original_price * percentage)
print("The sale price is: ", discount_price)