def calculator(number_x, number_y, operation):
	if operation=="add":
		a=number_x + number_y
		return a
	elif operation=="subtract":
		b=number_x - number_y
		return b
	elif operation=="multiply":
		c=number_x * number_y
		return c
	elif operation=="divide":
		d=number_x / number_y
		return d
e=calculator(20, 25, "add")
print  e

f=calculator(40, 3, "subtract")
print f

g=calculator(10, 4, "multiply")
print g

h=calculator(40, 4, "divide")
print  h

number_1=calculator(24, 20, "add")
print "add=", number_1

number_2=calculator(50, 60, "subtract")
print "subtract=", number_2

number_3=calculator(80, 120, "multiply")
print "multiply=", number_3

number_4=calculator(90, 23, "divide")
print "divide=", number_4



