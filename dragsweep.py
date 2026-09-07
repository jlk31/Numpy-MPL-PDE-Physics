#Plots acceleration vs velocity curves for bodies with different parameters
#Using the drag equation, see here https://en.wikipedia.org/wiki/Drag_equation

# Before running this check you have numpy and matplotlib installed by using pip freeze
# and reading the output

#  To change the parameters eg drag coeffs, SA, thrust etc,
#  go to the #PARAMETERS block and chaneg the values there.

#--------------------------------------------------------------------
# IMPORTS

import numpy as np                              #use pip install numpy if you don't have this
import matplotlib.pyplot as plt                 #use pip install matplotlib if you don't have this

#--------------------------------------------------------------------

#Calculate the accleration given input parameters (see wiki article above for explanation)
def accel_func(thrust, mass, C_d, CS_area, fluid_density, velocity):

    drag = 0.5 * C_d * CS_area * fluid_density * velocity ** 2

    accel = (thrust  - drag) / mass

    return(accel)


#PARAMETERS--------------------------------------------------------------------

#ENTER DRAG COEFF in the list variable "DRAG_COEFFICIENTS"
#drag coefficient 0.6 represents a boxy SUV eg Range Rover
#details here https://en.wikipedia.org/wiki/Drag_coefficient
#The 3 values here means the graph will have 3 lines. if you add more values to this list they will be automagically plotted.
DRAG_COEFFICIENTS = [0.4, 0.6, 0.8]

#cross sectional area in m^2
CS_area = 3

#fluid density in kgm^-3, 1.225 for air. If you want your body to move through something different, change this value.
fluid_density = 1.225

#relative wind in ms^-1   This will be the fastest the simulation will allow the body to go
#Remember the body might not actually reach this speed if its terminal velocity is lower than that.
#If the lines don't touch the x axis, increase this value
velocity_max = 30

#mass of the moving body in kg
mass = 2000

#Force propelling the body forwards in N
thrust = 500


#------------------------------------------------------------------------------
#This block actually creates the data
NO_OF_LINES = len(DRAG_COEFFICIENTS)

#Create velocity values as 1x50 array.  Documentation for np.linspace is here: https://numpy.org/doc/stable/reference/generated/numpy.linspace.html
velocity = np.linspace(0,velocity_max,50)

#calc acceleration values from velocity and put them in the list called "acceleration"

#initialise the list
acceleration = []

#calculate the accelerations
for i in range(NO_OF_LINES):

    acceleration.append(accel_func(thrust, mass, DRAG_COEFFICIENTS[i] , CS_area, fluid_density, velocity))
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#PLOTTING

#create graph
fig = plt.figure()
ax = plt.axes()

# Add a title so we know which it is
titlestring = f"""Acceleration with respect to velocity for a
streamlined body in air, $SA = {CS_area}m^2$"""

#put the title on the axes
plt.title(titlestring)




#------------------------------------------------------------------------------
#Set up the axes


#set axis limits
ax.set_xlim(0,max(velocity))
ax.set_ylim(0, 1.2* max(acceleration[0]))

#label axes
ax.set_xlabel(r'velocity $ms^{-1}$')
ax.set_ylabel(r'acceleration $ms^{-2}$')


#Axis ticks

#set x axis major tick
ax.xaxis.set_major_locator(plt.MultipleLocator(10))

#set x axis minor tick
ax.xaxis.set_minor_locator(plt.MultipleLocator(1))

#set y axis major tick
ax.yaxis.set_major_locator(plt.MultipleLocator(0.1))

#set y axis minor tick
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.01))


#Draw the axis lines
#NOTE: the first argument of ax.grid() was called "b" until matplotlib 3.5, where it
#was renamed to "visible". The old "b=True" spelling was removed in matplotlib 3.7 and
#now raises "ValueError: keyword grid_b is not recognized". See README.md.

#draw the x axis major lines
ax.grid(visible=True, which='major', axis='x', linestyle='-', linewidth=2)

#draw the x axis minor lines
ax.grid(visible=True, which='minor', axis='x', linestyle='-')

#draw the y axis major lines
ax.grid(visible=True, which='major', axis='y', linestyle='-', linewidth=2)

#draw the y axis minor lines
ax.grid(visible=True, which='minor', axis='y', linestyle='-')


#------------------------------------------------------------------------------

#plot lines
for i in range(NO_OF_LINES):
    ax.plot(velocity,acceleration[i], label = f"{DRAG_COEFFICIENTS[i]}")


#------------------------------------------------------------------------------


#plot the legend
plt.legend(title = "Drag coefficient")

#save the figure in the working directory.
#NOTE: this must happen BEFORE plt.show(), because show() hands the figure to the GUI
#and most backends clear it on close, which would save a blank image.
plt.savefig("drag_graph_Cd.png")

#render the plot on screen
plt.show()


#END----------------------------------------------------------------------------
