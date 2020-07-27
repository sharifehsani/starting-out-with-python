"""
- Author: Sharif Ehsani
- Date: June 2020
- www.gitbuh.com/ehsanis

3. Land Calculation
One acre of land is equivalent to 43,560 square feet. Write a program that asks the 
user to enter the total square feet in a tract of land and calculates the number of 
acres in the tract. Hint: divide the amount entered by 43,560 to get the number of
acres.
"""
feet = float(input("Enter the land size in Square feet and I tell you \
how much that is in acres: "))
acres = feet / 43560
print(feet, " square feet is: ", acres, "acres." )

