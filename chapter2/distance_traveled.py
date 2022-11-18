"""
- Author: Sharif Ehsani
- Date: June 2020
- https://github.com/sharifehsani

5. Distance Traveled
Assuming there are no accidents or delays, the distance that a car travels down the interstate
can be calculated with the following formula:
Distance =  Speed X Time

A car is traveling at 60 miles per hour. Write a program that displays the following:
• The distance the car will travel in 5 hours
• The distance the car will travel in 8 hours
• The distance the car will travel in 12 hours
"""
print("The car will travel differnet distances in different duration of times: ")
# a: 
speed = 60
time = 5
distance = speed * time
print("The car will travel ", distance, " km in", time, " hours ", "With the speed of ", speed , "km/h")

# b:
time = 8
distance = speed * time
print("The car will travel ", distance, " km in", time, " hours ", "With the speed of ", speed , "km/h")

# c:
time = 12
distance = speed * time
print("The car will travel ", distance, " km in", time, " hours ", "With the speed of ", speed , "km/h")
