# Write a function called isprime() that determines whether a number
# is prime or not, and returns either True or False accordingly. Redo
# Example 1.6.2 using this function. Try to make your program more
# efficient than the example, which is pretty dreadful in that regard!

# We'll use the sqrt(N) prime test.
# From http://stackoverflow.com/questions/5811151/why-do-we-check-upto-the-square-root-of-a-prime-number-to-determine-if-it-is-pri
# "If both a and b were greater than the square root of n, a*b would 
# be greater than n. So at least one of those factors must be less or 
# equal to the square root of n, and to check if n is prime, we only 
# need to test for factors less than or equal to the square root."


"""
This Python program determines whether a number
is prime or not . It is NOT the most efficient
way of determining whether a large integer is
prime! This will include improvements for this
particular program. 

The improvement being that instead of looping
up to the number N of interest we loop till sqrt(N)
only.
"""

def checkForPrime():

	# Start by getting the number that might be prime .
	Number = input( "What integer do you want to check?" )
	TestNumber = 2;

	# Main loop to test each number
	while TestNumber < sqrt(Number) :  #We loop up to 'sqrt(Number)' now, not just 'Number'.
		if (Number % TestNumber == 0):
		# The remainder is zero , so TestNumber is a factor
		# of Number and Number is not prime.
			print Number, " is divisible by ", TestNumber, "."
			# There is no need to test further factors.
			break
	
		elif (Number % TestNumber != 0):  #Getting sintax errors if I don't include this line.
			# The remainder is NOT zero , so increment
			# TestNumber to check the next possible factor .
			TestNumber += 1
	
	else :
		# We go there without finding a factor, so
		# Number is prime .
		print Number, " is prime. "
