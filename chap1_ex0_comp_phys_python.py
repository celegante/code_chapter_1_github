# Use a list comprehension to create a list of squares of the numbers
# between 10 and 20, including the endpoints.
"""
	This is the Python program solution for exercise 0 of chapter 1.
"""

minInteger = input("Input a starting positive minimum integer (try 10): ")
maxInteger = input("Input an ending positive maximum integer (try 20): ")

#ComputeListOfSquares is a function that computes the squares of a list of integers.
#maximunInteger is incremented for inclusion in the list of squares.
def ComputeListOfSquares(minimunInteger, maximunInteger):
	ListOfSquares = [ i**2 for i in range(minimunInteger, maximunInteger + 1, 1) ]
	return ListOfSquares

ListOfSquares = ComputeListOfSquares(minInteger, maxInteger)

#Print the list of squares.
for square in ListOfSquares:
	print square

