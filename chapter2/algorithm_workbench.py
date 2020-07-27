"""
- Author: Sharif Ehsani
- Date: June 2020
- www.gitbuh.com/ehsanis


QUESTION 1.
Write Python code that prompts the user to enter his or her height and assigns 
the user’s input to a variable named height
"""
height = int(input("Please enter your height and press enter: "))
print("you entered: ", height)

"""
QUESTION 2. 
Write Python code that prompts the user to enter his or her favorite color and 
assigns the user’s input to a variable named color.
"""
color = input("Enter your favorite color and press enter: ")
print("Your favorite color is: ", color)

"""
QUESTION 3. 
Write assignment statements that perform the following operations with the
variables a, b, and c.
a. Adds 2 to a and assigns the result to b
b. Multiplies b times 4 and assigns the result to a
c. Divides a by 3.14 and assigns the result to b
d. Subtracts 8 from b and assigns the result to a
"""
a = 0
b = a + 2
a = b * 4
b = a / 3.14
a = b - 8

"""
QUESTION 4.
Assume the variables result, w, x, y, and z are all integers, and that w = 5, x = 4,
y = 8, and z = 2. What value will be stored in result after each of the
following statements execute?
a. result = x + y
b. result = z * 2
c. result = y / x
d. result = y – z
e. result = w // z
"""
w = 5
x = 4
y = 8
z = 2
# a:
result = x + y
print("a: x + y = ", result)

#b:
result = z * 2
print("b: z * 2 = ", result)

#c:
result = y / x
print("c: y / x = ", result)

#d:
result = y - z
print("d: y - z = ", result)

#e:
result = w // z
print("e: w // z = ", result)

# QUESTION 5.
# Write a Python statement that assigns the sum of 10 and 14 
# to the variable total.

total = 10 + 14

# QUESTION 6
# Write a Python statement that subtracts the variable down_payment from the variable
# total and assigns the result to the variable due.

down_payment = 10
due = total - down_payment
