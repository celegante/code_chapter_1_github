# Write a program that takes a multi-digit integer and prints out its
# digits in English. Bonus point if the program takes care of ones/
# tens/hundreds/thousands properly.

"""
	This is the Python program solution for exercise 8 of chapter 1.
"""

# First we will check the pattern of the number expression, that is how many digits it has.
# From there we determine what dictionary of English numerals we should be using.
import numpy as np;

# Ask for a number in Python.
number =  input("Please enter a positive integer between 0 and 999999: ");

# We need to get the digits.
numberToString = str(number);
arrayOfDigits = array([int(i) for i in numberToString]);			

# We need to translate each digit to its respective ordinal number.
# Use the following dictionaries to spell out English numerals.
# Dictionary of units.
dictionaryOfUnits = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', 6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine' };

# Dictionary of teens. No pun intended.
dictionaryOfTeens = { 1 : 'eleven', 2 : 'twelve', 3 : 'thirteen', 4 : 'fourteen', 5 : 'fifteen', 6 : 'sixteen', 7 : 'seventeen', 
					  8 : 'eighteen', 9 : 'nineteen' };

# Dictionary of tenths.
dictionaryOfTens = { 1 : 'ten', 2 : 'twenty', 3 : 'thirty', 4 : 'forty', 5 : 'fifty', 6 : 'sixty', 7 : 'seventy', 8 : 'eighty', 9 : 'ninety'};


# Initialize string that will contain the number's English numeral.
numberInEnglishNumeralForm = '';
		   

# This is how you access an element of a dictionary: 'dictionaryOfTenths[num]'
# Maybe you can use modular arithmetic to solve the problem.

# Do a case for each of the digits, up to 6 digits are possible.
# Can you make this function smaller and less complex: more elegant?

def changeNumberToEnglishNumerals(arrayOfDigits):
	# Prints numerals for units.
	if ( len(arrayOfDigits) == 1 ):
		numberInEnglishNumeralForm = dictionaryOfUnits[arrayOfDigits[0]];
	
	# Prints numerals for numbers of the form 1x.
	elif ( len(arrayOfDigits) == 2 ) and ( arrayOfDigits[0] == 1 ) and ( arrayOfDigits[1] != 0 ):
		numberInEnglishNumeralForm = dictionaryOfTeens[arrayOfDigits[1]]; 
	
	# Prints numerals for multiples of ten.
	elif ( len(arrayOfDigits) == 2 ) and ( arrayOfDigits[1] == 0 ):
		numberInEnglishNumeralForm = dictionaryOfTens[arrayOfDigits[1]];
	
	# Prints numerals for two digits number besides -teens and multiples of ten.
	elif ( len(arrayOfDigits) == 2 ) and ( arrayOfDigits[1] != 0 ):
		numberInEnglishNumeralForm = dictionaryOfTens[arrayOfDigits[0]] + '-' + dictionaryOfUnits[arrayOfDigits[1]];		
		
	# Prints numerals for multiples of hundred.
	elif ( len(arrayOfDigits) == 3 ):
		numberInEnglishNumeralForm = dictionaryOfUnits[arrayOfDigits[0]] + ' hundred ' + changeNumberToEnglishNumerals( delete( arrayOfDigits, [0] ) );
		
	# Prints numerals for multiples of thousand.
	elif ( len(arrayOfDigits) == 4 ):
		numberInEnglishNumeralForm = dictionaryOfUnits[arrayOfDigits[0]] + ' thousand ' + changeNumberToEnglishNumerals( delete( arrayOfDigits, [0] ) );
		
	# Prints numerals for tens of thousands.
	elif ( len(arrayOfDigits) == 5 ) and ( arrayOfDigits[0] == 1 ) and ( arrayOfDigits[1] != 0 ):
		numberInEnglishNumeralForm = dictionaryOfTeens[arrayOfDigits[1]] + ' thousand ' + changeNumberToEnglishNumerals( delete( arrayOfDigits, [0,1] ) );
	
	elif ( len(arrayOfDigits) == 5 ) and  ( arrayOfDigits[1] == 0 ):
		numberInEnglishNumeralForm = dictionaryOfTens[arrayOfDigits[0]] + ' thousand ' + changeNumberToEnglishNumerals( delete( arrayOfDigits, [0,1] ) );
	
	elif ( len(arrayOfDigits) == 5 ) and ( arrayOfDigits[1] != 0 ):
		numberInEnglishNumeralForm = dictionaryOfTens[arrayOfDigits[0]] + '-' + dictionaryOfUnits[arrayOfDigits[1]] + ' thousand ' + changeNumberToEnglishNumerals( delete( arrayOfDigits, [0,1] ) );
		
	# Prints numerals for hundred thousands.
	elif ( len(arrayOfDigits) == 6 )  and ( arrayOfDigits[1] == 0 ) and ( arrayOfDigits[2] == 0 ): # For numbers like 800 234.
		numberInEnglishNumeralForm = dictionaryOfUnits[arrayOfDigits[0]] + ' hundred thousand ' + changeNumberToEnglishNumerals( delete( arrayOfDigits, [0, 1, 2] ));							
	
	elif ( len(arrayOfDigits) == 6 )  and ( arrayOfDigits[1] == 0 ) and ( arrayOfDigits[2] != 0 ): # For numbers like 804 234.
		numberInEnglishNumeralForm = dictionaryOfUnits[arrayOfDigits[0]] + ' hundred ' + dictionaryOfUnits[arrayOfDigits[2]] + ' thousand ' + changeNumberToEnglishNumerals( delete( arrayOfDigits, [0, 1, 2] ));
	
	elif ( len(arrayOfDigits) == 6 )  and ( arrayOfDigits[1] == 1 ) and ( arrayOfDigits[2] != 0 ): # For numbers like 817 234.
		numberInEnglishNumeralForm = dictionaryOfUnits[arrayOfDigits[0]] + ' hundred ' + dictionaryOfTeens[arrayOfDigits[2]] + ' thousand ' + changeNumberToEnglishNumerals( delete( arrayOfDigits, [0, 1, 2] ));
	
	elif ( len(arrayOfDigits) == 6 )  and ( arrayOfDigits[1] != 1 ) and ( arrayOfDigits[2] != 0 ): # For numbers like 845 234.
		numberInEnglishNumeralForm = dictionaryOfUnits[arrayOfDigits[0]] + ' hundred ' + dictionaryOfTens[arrayOfDigits[1]] + '-' + dictionaryOfUnits[arrayOfDigits[2]] + ' thousand ' + changeNumberToEnglishNumerals( delete( arrayOfDigits, [0, 1, 2] ));
	
	elif ( len(arrayOfDigits) == 6 )  and ( arrayOfDigits[1] != 1 ) and ( arrayOfDigits[2] == 0 ): # For numbers like 840 234.
		numberInEnglishNumeralForm = dictionaryOfUnits[arrayOfDigits[0]] + ' hundred ' + dictionaryOfTens[arrayOfDigits[1]] + ' thousand ' + changeNumberToEnglishNumerals( delete( arrayOfDigits, [0, 1, 2] ));
	
	return numberInEnglishNumeralForm

# Call the function to translate a number into its corresponding English numeral string.	
numberInWords = changeNumberToEnglishNumerals(arrayOfDigits)
	
print "The number %d is read as %s." % (number, numberInWords);