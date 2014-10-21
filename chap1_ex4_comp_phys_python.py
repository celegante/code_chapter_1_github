#Write a function for sinc(x) = sin(x) / x
#Make sure that your function handles x = 0 correctly.

#import pylab
from pylab import *

#Definition of sinc.
def sinc(x):
	if x == 0 :
		return 1  #The mathematical definition of sinc(x) of zero is 1'
	else :
		return sin(x)/x