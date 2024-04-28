# The Bungee jumper problem
# Enter the mass of the jumper
mass = float(input("Enter the mass of the object: "))
# the time to iterate to
time = int(input("Enter the time to iterate in seconds: "))
iterate = int(input("Enter the number for nth iteration: "))
# step or the difference in time interval
step = int(input("Enter the step size: "))
# the coeffocient of drag in air
coefficientOfDrag = 0.25
# acceleration due to gravity constant
g = 9.81
# initial velocity
v = 0
# error analysis
error = 0 
# number of iteraton made
iteration = 0
# increase to calculate the increase in step size
increase = 0
# iterations using while loop
while iteration < iterate:
    # Euler formular for calculating final velocity
    V = v + (g-coefficientOfDrag/mass * v**2)*step
    # error formular
    error = abs(V-v/V * 100)
    # iterations
    iteration += 1
    increase = increase + 2
    print(f"initial velocity:{v} final Velocity:{V} step:{increase} Error: {error}")
    # assigning the final velocity to the initial velocity for the next iteration
    v=V