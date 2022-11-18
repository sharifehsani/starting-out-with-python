"""
- Author: Sharif Ehsani
- Date: July 2020
- https://github.com/sharifehsani

6. Rewrite the following statements using augmented assignment operators.
a. x = x + 1
b. x = x * 2
c. x = x / 10
d. x = x - 100
"""

# main funciton to start the program
def main():
	# lets write some coded to actually check if it works in augmented assignment operation
	# everytime we increment or decrement the value of x changes, thats why lets use a,b,c,d variables

	a = 1
	print('original a value = ', a)
	a += 1				# x = x + 1
	print('(a = a + 1) or (a +=1) =', a)
	
	b = 2
	print('original b value = ', b)
	b *= 2				# x = x * 2
	print('(a = a * 2) or (a *=2) =', b)

	c = 40
	print('original c value = ', c)
	c /= 10
	print('(c = c / 10) or (c /= 10) =', c)


	d = 150
	print('original d value = ', d)
	d -= 100
	print('(d = d - 100) or (d -= 100) =', d)



	


# call the main function
main()
