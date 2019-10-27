number_x=int(raw_input("enter the first number="))
number_y=int(raw_input("enter the second numbe="))
operation=raw_input("enter the operation=")
def calculator(number_x, number_y, operation):
	if operation=="add":
		add=number_x + number_y
		return add
	elif operation=="subtract":
		subtract=number_x - number_y
		return subtract
	elif operation=="multiply":
		multiply=number_x * number_y
		return multiply
	elif operation=="divide":
		divide=number_x / number_y
		return divided
var=calculator(number_x, number_y, operation)
print var











