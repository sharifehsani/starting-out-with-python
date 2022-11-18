"""
- Author: Sharif Ehsani
- Date: June 2020
- https://github.com/sharifehsani
"""

print("this prints a new line at the end")
print("so thats why this line is printed")
print("this won't print new line at the end ->", end='')
print(" Thats why this line is not printed on a new line")
print("One", "Two", "Three")
print("Lets add / seperator between the arguments")
print("One", "Two", "Three", sep='/')
my_float = 123.4567453
print(format(my_float, '.2f'))
print("lets print 123.4567453 in scientific notation")
print(format(my_float, 'e'))
print("Lets add comma seperator in large numbers such as 1245356234.43434")
print(format(1245356234.43434, ',.2f'))
