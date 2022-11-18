"""
- Author: Sharif Ehsani
- Date: June 2020
- https://github.com/sharifehsani

6. Body Mass Index
Write a program that calculates and displays a person’s body mass index (BMI). The
BMI is often used to determine whether a person is overweight or underweight for his
or her height. A person’s BMI is calculated with the following formula:
BMI = weight * 703 / height2
where weight is measured in pounds and height is measured in inches.
"""

def main():
	display_message()


def display_message():
	print()
	print("Welcome, This program calculates a person’s Body Mass Index (MBI).")
	print("BMI is often used to determine whether a person is overweight or" + \
		" underweight for his/her height.")
	get_input()

def getSex():
	sex = input('Please specify your sex, choose "f" for Female and "m" for Male and press "Enter": ')
	return sex

def get_input():
	name = input("Plesase Enter your Name: ")
	if (name.lower()  == 'naz' or name.lower() == 'nazanin'):
		print("OH Hello Chumbagak!")
	else:
		print("OHH Hello ", name, "jan")

	print('Please choose the system of measurment.')
	measurment_system = input('Enter "m" for Metric = (Kilograms and Centimeters), or enter "i" for Imperial =' + \
			' (pounds and inches): ')
	if (measurment_system == "m"):
		print()
		#sex = input('Please specify your sex, choose "f" for Female and "m" for Male and press "Enter": ')
		sex = getSex()
		print(sex)
		while (sex != "f" and sex != "m"):
			sex = getSex()
		if (sex.lower() == "f"):
			pregnant = input('Are you pregnant? press "y" for yes and "n" for no: ')
			if (pregnant.lower() == "y"):
				sex_categorization()
		age = float(input('Please enter your age: '))
		if (age < 18 or age > 65):
			age_categorization()
		weight = float(input('Please enter your weight in Kilograms: '))
		height = float(input('Please enter your height in Centimeters: '))
		metric_bmi(age, weight, height)
	elif (measurment_system == "i"):					# Imperial System

		#sex = input('Please specify your sex, choose "f" for Female and "m" for Male and press "Enter": ')
		sex = getSex()
		while (sex != "f" and sex != "m"):
			sex = getSex()
		if (sex.lower() == "f"):
			pregnant = input('Are you pregnant? press "y" for yes and "n" for no: ')
			if (pregnant.lower() == "y"):
				sex_categorization()
		age = float(input('Please enter your age: '))
		if (age < 18 or age > 65):
			age_categorization()
		weight = float(input('Please enter your weight in pounds: '))
		height = float(input('Please enter your height in feet: '))
		imperial_bmi(age, weight, height)
	else:
		print("Wrong input please try again")
		get_input()
def metric_bmi(age, weight, height):
	if (age < 18 and age > 65):
		age_categorization(age)
	else:
		height_in_m = float(height / 100)
		bmi = weight / height_in_m ** 2
		bmi_categorization(bmi)
		

def imperial_bmi(age, weight, height):
	if (age < 18 and age > 65):
		age_categorization(age)
	else:
		height_in_inches = height * 12
		bmi = 703 * weight / (height_in_inches ** 2)
		bmi_categorization(bmi)
	
def sex_categorization():
	print("Congratulations on your pregnancy!, But sorry, this BMI nomogram is not intended for use with: Pregnant" + \
				" and lactating women")
	exit()

def bmi_categorization(bmi):

	normal = False

	if (bmi < 18.5 ):
		print("Your Body Mass Index (BMI) is :", format(bmi, '.2f'))
		print('You are classified as "underweight". You have an "Increased Risk of developing health problems"!.')
		normal = False
		source(normal)

	elif (bmi >= 18.5 - bmi <= 24.9):
		print("Your Body Mass Index (BMI) is :", format(bmi, '.2f'))
		print("Congratulations!, your weight is normal. Keep the good work up.")
		normal = True
		source(normal)
		
	elif(bmi >= 25 and bmi <= 29.9):
		print("Your Body Mass Index (BMI) is :", format(bmi, '.2f'))
		print('You are classified as "overweight". You have an "Increased Rish of developing health problems"!.')
		normal = False
		source(normal)

	elif(bmi >= 30.0 and bmi <= 34.9):
		print("Your Body Mass Index (BMI) is :", format(bmi, '.2f'))
		print('You are classified as "Obese class I". You have an "HIGH Rish of developing health problems"!.')
		normal = False
		source(normal)

	elif(bmi >= 35.0 and bmi <= 39.9):
		print("Your Body Mass Index (BMI) is :", format(bmi, '.2f'))
		print('You are classified as "Obese class II". You have an "VERY HIGH Rish of developing health problems"!.')
		normal = False
		source(normal)

	elif(bmi >= 40.0):
		print("Your Body Mass Index (BMI) is :", format(bmi, '.2f'))
		print('You are classified as "Obese class III". You have an "EXTEREMELY HIGH Rish of developing health problems"!.')
		normal = False
		source(normal)
		

def age_categorization():
	
	print("Sorry, This BMI nomogram is not intended for use with:")
	print("those under 18 years of age.")
	print("Note: For persons 65 years and older the 'normal' range may begin slightly above BMI 18.5\nand extend into the " + \
			"'overweight' range.")
	exit()

def source(normal):
	if (normal == True):
		print("Source: Health Canada. Canadian Guidelines for Body Weight Classification in Adults. Ottawa:\nMinister of" + \
			" Public Works and Government Services Canada; 2003.")
		print("To clarify risk for each individual, other factors such as lifestyle habits, fitness level, and\npresence or" + \
			" absence of other health risk conditions also need to be considered.")
	else:
		print("Please refer to the Government of Canada's health, food and nutrition guid at:")
		print("https://www.canada.ca/en/services/health.html")
		print("Source: Health Canada. Canadian Guidelines for Body Weight Classification in Adults. Ottawa: Minister of" + \
			" Public Works and Government Services Canada; 2003.")
		print("Oh hey, Thank you for using my BMI program")
		print()


main()
