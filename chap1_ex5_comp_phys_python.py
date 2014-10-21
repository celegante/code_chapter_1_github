#It is good practice to
#include such a comment at the beginning of each Python program. This
#comment should include a brief description of the program, instructions on
#how to use it, and the author & date.

#Write a function that calculates the value of the nth triangular number.
#Triangular numbers are formed by adding a series of integers from 1
#to n: i.e. 1 + 2 + 3 + 4 = 10 so 10 is a triangular number, and 15 is
#the next triangular number after 10.

#import pylab
from pylab import *

def triangularNumber(n):
	if n == 0 :
		return 0  
	else :
		return (n*(n+1))/2