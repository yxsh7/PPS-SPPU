"""
To accept an object mass in kilograms and velocity in meters per second and display its 
momentum. Momentum is calculated as e=mc2 where m is the mass of the object and c is 
its velocity. 
"""

# INPUT
object_mass = int(input("Enter mass in Kilograms"))
Velocity = int(input("Enter Velocity in meters per second"))

# CALCULATE

momentum = object_mass * (Velocity * Velocity)

# DISPLAY 
print("MOMENTUM =", momentum)
