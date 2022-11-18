

"""
- Author: Sharif Ehsani
- Date: July 2020
- https://github.com/sharifehsani

In the Spotlight:
Modularizing with Functions
Hal owns a business named Make Your Own Music, which sells guitars, drums, banjos,
synthesizers, and many other musical instruments. Hal’s sales staff works strictly on commission.
At the end of the month, each salesperson’s commission is calculated according to
Table 6-1.
Table 6-1 Sales commission rates
Sales This Month Commission Rate
Less than $10,000 10%
$10,000–14,999 12%
$15,000–17,999 14%
$18,000–21,999 16%
$22,000 or more 18%
Because the staff gets paid once per month, Hal allows each employee to take up to $2,000
per month in advance. When sales commissions are calculated, the amount of each employee’s
advanced pay is subtracted from the commission. If any salesperson’s commissions are less
than the amount of their advance, they must reimburse Hal for the difference. To calculate
a salesperson’s monthly pay, Hal uses the following formula:
pay = sales * commission rate - advanced pay
"""

# main function to start the program
def main():
	print("This program calculates the monthly pay of a salesperson who is strictly commission based.")
	# pay formula: pay = sales * commission rate - advanced pay

	# call the get_input function to get user's monthly sale and advanced pay
	monthly_sale, advanced_pay = get_input()

	# call the commision() function to calculate the commission and pass the monthly sale as parameter
	commissionPay = commission(monthly_sale)

	# call the calculate_pay function ()passing commissionPay and monthly sale and advanced py as arguments
	pay = calculate_pay(commissionPay, advanced_pay)

	# print the result out
	print("--------------------------")
	print("Your monthly sale is: $", format(monthly_sale, '.2f'), sep='')
	print("Your have taken: $", format(advanced_pay,'.2f'), " as advanced payment", sep='')
	print("Your monthly pay is: $", format(pay,'.2f'), sep='')




# function to get user input
def get_input():
	monthlySale = float(input("Enter employee’s monthly sale: "))
	advancedPay = float(input("Enter employee's advanced pay: "))
	return monthlySale, advancedPay
	# end of function


# function to calculate commision
def commission(sale):
	commission_pay = 0.0

	if (sale < 10000):
		commission_pay = sale * 0.10
	elif (sale >= 10000 and sale <= 14999):
		commission_pay = sale * 0.12
	elif (sale >= 15000 and sale <= 17999):
		commission_pay = sale * 0.14
	elif (sale >= 18000 and sale <= 21999):
		commission_pay = sale * 0.16
	else:
		commission_pay = sale * 0.18

	return commission_pay
	# end of function

# function to calculate the pay
def calculate_pay(commissionPay, advanced_pay):
	return (commissionPay - advanced_pay)



# call the main function
main()
