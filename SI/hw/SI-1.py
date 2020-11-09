"""This program calculates the approximate exponential growth of the proposed virus."""

"""This program outputs the results of the request into a CSV file with a {space} delimiter to
be used in other programs or in any other way you see fit. By default this program exports the data in a (2,x)
array where x is dependant on the number of days the simulation is run for and the polling rate of the program.
To instead export in a (x, 2) format simply uncomment line 46."""

""""To rename the output file simply change the name on line 47. To toggle between first and second order models,
change the saved array on line 47"""

import numpy as np

howlong = int(input("How many days should this simulation be run for? Use an Integer"))

def first_order_model(alpha, deltat):
    y = 1
    t = 0
    Fycurrent = [1]
    Ftcurrent = [0]
    while t + deltat <= howlong:
        y = (1 + alpha*deltat)*y
        t += deltat
        Ftcurrent.append(t)
        Fycurrent.append(y)
    FtyConc = np.array([Ftcurrent, Fycurrent])
    return FtyConc

def second_order_model (alpha, deltat):
    y = 1
    t = 0
    Sycurrent = [1]
    Stcurrent = [0]
    while t + deltat <= howlong:
        diff = alpha*deltat/2
        growthfactor = (1 + diff)/(1 - diff)
        y = y * growthfactor
        t += deltat
        Sycurrent.append(y)
        Stcurrent.append(t)
    StyConc = np.array([Stcurrent, Sycurrent])
    return StyConc

FOMeq = first_order_model(1, 0.1)
SOMeq = second_order_model(1, 0.1)
#FOMeq = np.transpose(FOMeq)
np.savetxt('FiniteDiffSOMPoint1.csv', SOMeq)
