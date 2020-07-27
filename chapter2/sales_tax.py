"""
- Author: Sharif Ehsani
- Date: June 2020
- www.gitbuh.com/ehsanis

6. Sales Tax
Write a program that will ask the user to enter the amount of a purchase. The program
should then compute the state and county sales tax. Assume the state sales tax is 4 percent
and the county sales tax is 2 percent. The program should display the amount of the purchase,
the state sales tax, the county sales tax, the total sales tax, and the total of the sale
(which is the sum of the amount of purchase plus the total sales tax).
Hint: use the value 0.02 to represent 2 percent, and 0.04 to represent 4 percent.
"""

purchase_amount = float(input("Enter purchase amount: "))
pst = 0.04 * purchase_amount			# provincial sales tax
gst = 0.02 * purchase_amount		# government sales tax

print("Purchase amount: ", purchase_amount)
print("PST @ 4%: ", pst)
print("GST @ 2%: ", gst)
print("Total Sales Tax @ 6%: ", pst+gst)
print("Total sale: ", purchase_amount + pst + gst)

