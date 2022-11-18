"""
- Author: Sharif Ehsani
- Date: June 2020
- https://github.com/sharifehsani

4. Automobile Costs
Write a program that asks the user to enter the monthly costs for the following expenses
incurred from operating his or her automobile: loan payment, insurance, gas, oil, tires, and
maintenance. The program should then display the total monthly cost of these expenses,
and the total annual cost of these expenses.
"""

def main():

	print("This program will calculate total monthly and yearly cost that your Automobile incure.")
	loan = float(input("Enter your monthly loan payment: "))
	insurance = float(input("Enter your monthly insurance payment: "))
	gas = float(input("Enter your monthly gas payment: "))
	tires = float(input("Enter your monthly oil payment: "))
	oil = float(input("Enter your monthly tires payment: "))
	maintenance = float(input("Enter your monthly maintenance payment: "))
	monthly_cost(loan, insurance, gas, tires, oil, maintenance)
	yearly_cost(loan, insurance, gas, tires, oil, maintenance)

def monthly_cost(loan, insurance, gas, tires, oil, maintenance):
	total_monthly_cost = loan + insurance + gas + tires + oil + maintenance
	print("Your automobile costs you ", total_monthly_cost, " a month")



def yearly_cost(loan, insurance, gas, tires, oil, maintenance):
	total_yearly_cost = 12 * (loan + insurance + gas + oil + maintenance)
	print("Your automobile costs you ", total_yearly_cost, " a year")


main()
