#   ---TEMPERATURE CONVERTER---
#imports time modules to work implement time within the program
import time 

#greet the user
print("Hello, Welcome to the Temperature Converter Widget")
print("-" *30)

#makes the program pause for 2 seconds
time.sleep(2) 

#variable for while loop to use to know when to terminate the widget
running = True 

#variable that holds a list of acceptable options a user may choose
valid_options = ['f', 'c', 'k'] 


#while loop for the widgets checks and calculations
while running: 
	print("-" *30)
	time.sleep(1)
	option = input("Please select an option. \n 'F' for Fahrenheit \n 'C' for Celsius \n 'K' for Kelvin \n 'Quit' to exit the widget \n: " ).strip().lower()
	#time.sleep(1)

#ends the loop by changing the running value to False
	if option == 'quit': 
		running = False
		print("\n Thanks for using the temperature converter widget")
		time.sleep(1)
#continue to the next phase of the while loop, if any
		continue 

#checks if option entered is within the valid options variable, if not, it prompts user to select a valid one
	if option not in valid_options: 
		print("\n Please enter a valid option.")
		time.sleep(1)
		continue

#creates a 'try' block that tells the program to 'try' the below if/elif statements
	try:

#'if' the user chose option 'f'
		if option == 'f':
#takes in user input for temperature they want to convert
			fahrenheit = float(input("\n please enter the temperature in fahrenheit. \n: "))
			time.sleep(1)
#temperature conversion calculations
			celsius = (fahrenheit - 32) * 5/9
			kelvin = (fahrenheit - 32) * 5/9 +273.15
#prints out the conversion using an F string in order to format the information within the output string
			print(f"\n {fahrenheit:.2f}℉ is equal to {celsius:.2f}℃ and equal to {kelvin:.2f}K")
			time.sleep(2)

#else if the user chose option 'c'
		elif option == 'c':
			celsius = float(input("\n please enter the temperature in celcius. \n: "))

			fahrenheit = (celsius * 9/5) + 32
			kelvin = celsius + 273.15
			print(f"\n {celsius:.2f}℃ is equal to {fahrenheit:.2f}℉ and equal to {kelvin:.2f}K")
			time.sleep(2)

		elif option == 'k':
			kelvin = float(input("\n please enter the temperature in kelvin. \n: "))

			fahrenheit = (kelvin - 273.15) * 9/5 + 32
			celsius = kelvin - 273.15
			print(f"\n {kelvin:.2f}K is equal to {celsius:.2f}℃ and equal to {fahrenheit:.2f}℉")


#if the program tries the previous 'try' block statements and gets a invalid input, it prevents the program from crashing
#and instead provides a error message
	except ValueError:
		print("\n invalid temperature input. please enter a number")
