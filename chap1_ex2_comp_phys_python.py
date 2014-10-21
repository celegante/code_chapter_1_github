# For the model used in introductory physics courses, a projectile thrown
# vertically at some initial velocity vi has position 
# y(t) = yi + vi*t − (1/2)*g*t^2, where g = 9.8 m/s. 
# Write a Python program that creates two lists,
# one containing time data (50 data points over 5 seconds) and the other
# containing the corresponding vertical position data for this projectile.
# The program should ask the user for the initial height yi and initial
# velocity vi, and should print a nicely-formatted table of the list values
# after it has calculated them.

"""
	This is the Python program solution for exercise 2 of chapter 1.
"""

#Ask the user to provide the initial state of the projectile.
initialHeight = input("Please provide the initial height, in meters, of the projectile: ")
initialVelocity = input("Please provide the initial velocity, in meters per second, of the projectile: ")

#Gravitational acceleration.
g = 9.8

# The time array contains (N=50) 50 data points over 5 seconds.
startingTime = 0.0
endingTime = 5.0
N = 50


#If you use a list comprehension array for the time, you can't include the endingTime, 
#i.e. [i*timeResolution for i in range(startingTime, endingTime+1, 1) ] 
time = linspace(startingTime, endingTime, N)

#This is the position computation for a particle 
position = initialHeight + initialVelocity*time - (9.8/2) * time**2

#We now create a list of tuples so that we can access it with a single for. 
time_position_tuple = zip(time, position)

#Here's a nicely formated table with the position and times of the particle.
print "Time (s)		Position (m)"

#Here are the formatted time and space coordinates of the particle.
for i in range(0, N):
	print "%0.2f		        %0.2f"	% (time_position_tuple[i][0], time_position_tuple[i][1])