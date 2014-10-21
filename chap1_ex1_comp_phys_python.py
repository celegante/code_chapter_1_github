# Use a list comprehension to create a list of squares of the numbers
# between 10 and 20, including the endpoints.
#Write a Python program to print out the first N numbers in the Fibonacci sequence. 
#The program should ask the user for N , and should
#require that N be greater than 2.

"""
	This is the Python program solution for exercise 1 of chapter 1.
"""

DesiredFibonacciNumber = 0

#Make sure the user inputs a numer greater than 2 as specified by the user.
while ( DesiredFibonacciNumber <= 2 ) :
	DesiredFibonacciNumber = input("Please input an integer N greater than 2, so that the Nth Fibonacci number is computed. ")

#The function BinetFibonacciFormula uses Binet's formula to calculate the Nth Fibonacci number.
def BinetFibonacciFormula(N):
	phi = (1.0 + sqrt(5.0))/2.0;
	psi = (1.0 - sqrt(5.0))/2.0;
	delta = phi - psi
	
	Fibonacci = int ( floor( ( (phi**N)-(psi**N) ) / delta ) ) #This is Binet's formula. We floor the result and turn it into an integer.
	return Fibonacci

FibonacciResult = BinetFibonacciFormula(DesiredFibonacciNumber)
	
print "The %dth Fibonacci number is %d." % (DesiredFibonacciNumber, FibonacciResult)