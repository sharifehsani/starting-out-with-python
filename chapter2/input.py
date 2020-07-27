"""
- Author: Sharif Ehsani
- Date: June 2020
- www.gitbuh.com/ehsanis

"""
sex = ""

print("Please fill out the following infomation:")
fname = input("First name: ")
lname = input("Last name: ")
gender = input("sex: m = male, f = female, o = others ")
month = input("Month of birth in the form of 1,2...,12: ")
day = input("Birth day in the form of 1,2,3...,31: ")
year = input("Year of birth: ")
phone = input("Phone number: ")

details = {"First_name":fname, last_name:lname, sex: sex, month:month, day:day, Year: year}
print("Address: ")
street_number = input("Street Number: ")
street_name = input("Street Name: ")
unit = input("Unit number: ")
city = input("City: ")
province = input("Province/Teritory: ")
p_code = input("Postal Code: ")
country = input("Country")
address = [unit, street_number, street_name, city, province, p_code, country]
student_id = input("Please enter your student ID: ")

print()
print("Here is your complete information:")
for x in details:
	"""
	if  details[2] == 'f':
		details[2] = "female"
	if details[2] == 'm':
		details[2] = "male"
	else:
		details[2] = "Other"
		"""
	print(x)


