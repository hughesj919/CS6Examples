"""Question 2.2: Write a program that examines three variables--x,y, and z-- 
   and prints the largest odd number among them. If none of them are odd, 
   it should print a message to that effect.
"""

x = int(input("Enter a number for x: "))
y = int(input("Enter a number for y: "))
z = int(input("Enter a number for z: "))

# Here we are assigning boolean values to each variable x_is_odd, y_is_odd, etc
x_is_odd, y_is_odd, z_is_odd = (x % 2 != 0), (y % 2 != 0), (z % 2 !=0) 

# no odds
if not x_is_odd and not y_is_odd and not z_is_odd:
	print("There are no odds.")
# x is only odd
elif x_is_odd and not y_is_odd and not z_is_odd:
	print(str(x) + " is the largest odd.")
# y is only odd
elif not x_is_odd and y_is_odd and not z_is_odd:
	print(str(y) + " is the largest odd.")
# z is only odd
elif not x_is_odd and not y_is_odd and z_is_odd:
	print(str(z) + " is the largest odd.")
# x and y are odd
elif x_is_odd and y_is_odd and not z_is_odd:
		if x > y:
			print(str(x) + " is the largest odd.")
		else:
			print(str(y) + " is the largest odd.")
# y and z are odd
elif not x_is_odd and y_is_odd and z_is_odd:
		if y > z:
			print(str(y) + " is the largest odd.")
		else:
			print(str(z) + " is the largest odd.")
# x and z are odd
elif x_is_odd and not y_is_odd and z_is_odd:
		if x > z:
			print(str(x) + " is the largest odd.")
		else:
			print(str(z) + " is the largest odd.")
# x and y and z are odd
else:
	if x >= y and x >= z:
		print(str(x) + " is the largest odd.")
	elif y >= x and y >= z:
		print(str(y) + " is the largest odd.")
	else:
		print(str(z) + " is the largest odd.")
