# Write a Python program to make an N × N multiplication table and
# write this table to a file. Each row in the table should be a single line
# of the file, and the numbers in the row should be tab-delimited. Write
# the program so that it accepts two parameters when invoked: the size
# N of the multiplication table and the filename of the desired output
# file. In other words, the command to make a 5 × 5 table saved in file
# table5.txt would be << timestable.py 5 table5.txt >>

"""
	This is the Python program solution for exercise 7 of chapter 1.
"""

from pylab import *

# Ask for what number's multiplication table the user wishes to create.
DesiredMultiplicationTableNumber = input('What is the multiplication table you want to generate?: ');

# Ask for the file's name.
MultiplicationTableFileName = raw_input('What is the name of the file you want to generate?: ');
MultiplicationTableFileName = 'C:\OpenWormMatlab\OpenWormAcademy2014\Home_work\hw3\code_chapter_1\\' + str(MultiplicationTableFileName);

MultiplicationTableFileHandle = open(MultiplicationTableFileName, 'w');

# Writing the lines of the multiplication table. Using a 'with' statement.
# No working when using the << with open('MultiplicationTableFileName', 'w') as MultiplicationTableFileHandle : >>
for i in range(1, DesiredMultiplicationTableNumber + 1):
	for j in range(1, DesiredMultiplicationTableNumber + 1):
		new_str = str(i) + ' x ' + str(j) + ' = ' + str(i*j) + '\n';
		MultiplicationTableFileHandle.write(new_str)

MultiplicationTableFileHandle = close()
		
print 'File %s is saved.' % (MultiplicationTableFileName)