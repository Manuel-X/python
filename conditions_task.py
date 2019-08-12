first_number = input("Enter the first number:  ")
second_number = input("Enter the second number:  ")
operation = input("Choose the opertaion (+, -, /, *):")

if first_number.isdigit() and second_number.isdigit():
	if operation == "+":
		print ("The answer is " + str( int(first_number) + int(second_number) ) )
	elif operation == "-":
		print ("The answer is " + str( int(first_number) - int(second_number) ) )
	elif operation == "/":
		print ("The answer is " + str( int(first_number) / int(second_number) ) )
	elif operation == "*":
		print ("The answer is " + str( int(first_number) * int(second_number) ) )
	else:
		print ('operation "{}" is not valid'.format(operation))
else:
	print ("the numbers were invalid") 