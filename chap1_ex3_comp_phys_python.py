# The energy levels for a quantum particle in a three-dimensional rectangular 
# box of dimensions {L1, L2, and L3} are given by 
#
# E(n1,n2,n3) = ( ((h/2π)**2)*(π**2)/(2*m) ) ( (n1/L1)**2 + (n2/L2)**2 + (n3/L3)**2 )
#
#where the n’s are integers greater than or equal to one. Write a program that will calculate, and list in order of increasing energy, the
#values of the n’s for the 10 lowest different energy levels, given a box
#for which L2 = 2*L1 and L3 = 4*L1.

"""
	This is the Python program solution for exercise 3 of chapter 1.
"""

# The program will calculate the energy of the confined particle for an indefinite mass 'm' and box dimension 'L1'.
# If values for these parameters are provided, we must take the energy result and divide it by 1/(m * L1**2).

import numpy;

# Planck's constant is 6.62e-34 J/s.
h = 6.62e-34;

# Up to what max integer value do we want to explore the range of energy levels.
# Without including this very integer.
Nmax = 5;

# Initialize the list of integer arrays.
ListOfIntegerTuplesAndEnergy = [];

# The function QuantumEnergyParticleInBox calculates for L2 = 2*L1 and L3 = 4*L1 the particle's free energy levels.
def QuantumEnergyParticleInBox(integerTuple):
  E = ( ((h/(2*pi))**2) * (pi**2)/(2) ) * ( (integerTuple[0])**2 + ((integerTuple[1])**2)/4 + ((integerTuple[2])**2)/16 )
  return E

# Form an array of integer arrays [i,j,k] and their corresponding energies.
for i in range(1, Nmax) :
	for j in range(1, Nmax) :
		for k in range(1, Nmax) :
			ListOfIntegerTuplesAndEnergy.append( [[i, j, k], QuantumEnergyParticleInBox( [i,j,k] )] )

# Sort the energy levels and select the first 10 levels of energy. Permutations are not important.
# Use the append number to create the list. A more efficient sort should be used. Bubble sort has 
# a worst case performance of O(n**2), n is the size of the list. I know it sucks, but I can implement a better
# sort algorithm later.
def bubbleSortComplex(List):
	for k in range(0, (size(List)/2) - 1):	#Size of this double list is 128, but each entry of the indices can only go as far as 64.
		for i in range(0, (size(List)/2) - 1 ):
			temp = List[i][1];	
			if	List[i][1] > List[i+1][1]:
				temp = List[i][1];
				List[i][1] = List[i+1][1];
				List[i+1][1] = temp;
	return List

sortedEnergyArray = bubbleSortComplex(ListOfIntegerTuplesAndEnergy);

# This is the list of the degenerate levels of energy. Only the 10 highest energies are printed. Only print up to [3,2,4].
# Is there a less manual way of doing this? That is to algorithmically specify that print outs should be only up to [3,2,4]. This is element 40

print "The ten first energy levels with their respective degeneracies are: \n"

for i in range(0,43) :
	print sortedEnergyArray[i]