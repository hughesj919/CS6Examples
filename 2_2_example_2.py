"""Question 2.2: Write a program that examines three variables--x,y, and z-- 
   and prints the largest odd number among them. If none of them are odd, 
   it should print a message to that effect.
"""
# Read the program starting from line 31 and then come back to this function.
# This is just a function definition we will use later
def example_2(x, y, z):
	# put our variables into a list so we can iterate through them later
	nums = [x, y, z]

	# make a set for storing just the odds. sets are unordered groups of items with 
	# no duplicates
	odds = set()

	# iterate through, add the odds to our set
	for num in nums:
		if num % 2 != 0:
			odds.add(num)

  # if we found no odds, print a message saying so and return nothing from the function
	if len(odds) == 0:
		print("There are no odds.")
		return None
	else:
		# if we have odds, we find the largest odd in our set using the max
		largest = max(odds)
		print(str(largest) + " is the largest odd.")
		return largest


# This is standard boilerplate code for python that means "the program starts here".
if __name__ == '__main__':
	
	# Gather the user input
	x = int(input("Enter x: "))
	y = int(input("Enter y: "))
	z = int(input("Enter z: "))

	# Call the example_2 function with our gathered inputs
	example_2(x, y, z)

