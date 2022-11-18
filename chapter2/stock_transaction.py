"""
- Author: Sharif Ehsani
- Date: June 2020
- https://github.com/sharifehsani

10. Stock Transaction Program
Last month Joe purchased some stock in Acme Software, Inc. Here are the details of the
purchase:
• The number of shares that Joe purchased was 1,000.
• When Joe purchased the stock, he paid $32.87 per share.
• Joe paid his stockbroker a commission that amounted to 2 percent of the amount he paid
for the stock.
Two weeks later Joe sold the stock. Here are the details of the sale:
• The number of shares that Joe sold was 1,000.
• He sold the stock for $33.92 per share.
• He paid his stockbroker another commission that amounted to 2 percent of the amount
he received for the stock.

Write a program that displays the following information:
• The amount of money Joe paid for the stock.
• The amount of commission Joe paid his broker when he bought the stock.
• The amount that Joe sold the stock for.
• The amount of commission Joe paid his broker when he sold the stock.
• Display the amount of money that Joe had left when he sold the stock and paid his
broker (both times). If this amount negative, then Joe lost money.
"""

#purchased share details

shares_bought = 1000
price_per_share_bought = 32.87
total_share_price_bought = shares_bought * price_per_share_bought
commission_bought = 0.02 * total_share_price_bought

#sold share details
share_sold = 1000
price_per_share_sold = 33.92
total_share_price_sold = share_sold * price_per_share_sold
commission_sold = total_share_price_sold * 0.02

print("You paid $",format(total_share_price_bought, '.2f'), " for the stock.")
print("You paid $",format(commission_bought, '.2f'), " as a commission to the broker.")
print("You received $",format(total_share_price_sold, '.2f'), " for selling the stock.")
print("You paid $",format(commission_sold, '.2f'), " to the broker for selling your stock.")

total_paid = total_share_price_bought + commission_bought
total_recieved = total_share_price_sold - commission_sold

benifit = total_recieved - total_paid

if (benifit < 0):
	print("Sorry you are at lose!, you lost: ", format(benifit, '.2f'), " in this stock exchange")
else:
	print("Horray, you benifited from this stock transaction and here is your gain: ", benifit)
