"""Calculates the error relating to finite differences of differential
equations, specifically in approximating cos(x) and exponential growth"""

import math
import matplotlib.pyplot as plt
import numpy as np


def time_vals(delta):
    """Returns a list of the values of t to be used in RHS

    Parameters
    ----------
    delta : float
        Used to calculate how many time values are in a given interval

    Returns
    -------
    numpy.ndarray
        A numpy array of time values between 0 and 2*pi with interval delta


    """
    return np.arange(0, 2*math.pi, delta)


def x_vals(delta):
    """Returns a list of the x values for use in RHS calculation

    Parameters
    ----------
    delta : float
        Used to calculate how many x values are in a given interval

    Returns
    -------
    np.ndarray
        The x values for which the values of the calculation are to be plotted

    """
    return np.arange(0 + delta/2, 2*math.pi + delta/2, delta)


def calc(delta):
    """Returns a list of y values to approximate the function cos(x)

    Parameters
    ---------
    delta : float
        Passed to the time_vals() function

    Returns
    -------
    numpy.ndarray
        The y values of the approximated function with a certain value of delta

    """
    return (np.sin(time_vals(delta)+delta)-np.sin(time_vals(delta)))/delta


plt.plot(x_vals(1), calc(1), label="d = 1")
plt.plot(x_vals(1/2), calc(1/2), label="d = 1/2")
plt.plot(x_vals(1/3), calc(1/3), label="d = 1/3")
plt.plot(x_vals(1/10), np.cos(x_vals(1/10)), label="cos(x)")
plt.legend(loc="best")
plt.title("Approximating cos(x) with various delta x")
plt.show()

COMMON_DELTA = 0.1
INFECTIONS = 1


def time(delta):
    """Returns a list of time values used for x values of the graph

    Parameters
    ----------
    delta : float
        Used to create value in a given interval with spacing of delta

    Returns
    -------
    numpy.ndarray
        Values in a certain interval seperated by value delta

    """
    return np.arange(0, 5, delta)


def first(first_infections, delta):
    """"Returns a list of y values approximating the first order equation"

    Parameters
    ----------
    first_infections : float
        Represents the value of alpha used in the approximation
    delta : float
        Passed to time_vals and used in the approximation

    Returns
    -------
    numpy.ndarray
        A list of y-values of the first order approximation through time

    """
    y_vals = []
    y_old = 1
    for count in time(delta):
        y_new = (1 + first_infections * delta) * y_old
        y_vals.append(y_new)
        y_old = y_new
    return y_vals


def second(second_infections, delta):
    """Returns a list of y values approximating the second order equation

    Parameters
    ----------
    second_infections : float
        Represents the value of alpha used in the approximation
    delta : float
        Passed to time_vals and used in the approximation

    Returns
    -------
    numpy.ndarray
        A list of y values of the second order approximation through time

    """
    y_vals = []
    y_old = 1
    for time_count in time(delta):
        temp = 0.5 * delta * second_infections
        y_new = y_old * ((temp + 1) / (1 - temp))
        y_vals.append(y_new)
        y_old = y_new
    return y_vals


def precise(precise_infections, delta):
    """Returns a list of y values for the exact growth function e ^ (a * t)

    Parameters
    ----------
    precise_infections : float
        Represents the value of alpha used in e ^ a * t
    delta : float
        Passed to time_vals

    Returns
    -------
    numpy.ndarray
        A list of y values of the approximation through time

    """
    return np.exp(precise_infections*time(delta))


def error_precise(order, error_infections):
    """Returns a list of y values

    Calculates the difference between the first or second order equations
    and the precise growth graph with respect to time

    Parameters
    ----------
    order : function
        Passed as the function (first or second) that will be used for approx.
    error_infections : float
        Used in the approximations and the precise calculations as alpha

    Returns
    -------
    numpy.ndarray
        The absolute value of the difference between precise calculation
        and approximatinon through time

    """
    return abs(precise(error_infections, COMMON_DELTA) -
               order(error_infections, COMMON_DELTA))


def delta_vals():
    """Returns a list of delta time values used to calculate error

    Returns
    -------
    numpy.ndarray
        Values used for delta that are very nearly divisible into 5

    """
    nums = []
    for exponent in np.arange(-0.09, 2.0, 0.000001):
        if 5.0 % (1/10)**exponent < 0.00001:
            nums.append((1/10)**exponent)
    return nums


def error_delta(order):
    """Returns a list of y values of error

    Error is calculated between the first or second
    order equations and the exact growth at t = 5 with repsect to
    exponentially smaller values of delta t used to approximate

    Parameters
    ----------
    order : function
        The order that will be approximated against the precise growth

    Returns
    -------
    numpy.ndarray
        The difference very near t = 5 between the approximation
        and the precise growth with respect to delta t used to approximate

    """
    temp_infections = 1
    y_vals = []
    for delta in delta_vals():
        y_vals.append(abs(math.exp(5*temp_infections) -
                          order(temp_infections, delta)[-2]))
    return y_vals


plt.figure()
plt.plot(time(COMMON_DELTA), first(INFECTIONS, COMMON_DELTA),
         label="1st order")
plt.plot(time(COMMON_DELTA), second(INFECTIONS, COMMON_DELTA),
         label="2nd order")
plt.plot(time(0.1), precise(INFECTIONS, 0.1), label="Exact model")
plt.xlabel("Time (days)")
plt.ylabel("Number of infections")
plt.legend(loc="best")
plt.title(f"Disease growth approximation, \
          1st and 2nd order (a = {INFECTIONS})")
plt.show()

plt.figure()
plt.plot(delta_vals(), error_delta(first), label="1st order")
plt.plot(delta_vals(), error_delta(second), label="2nd order")
plt.xlabel("Delta t (days)")
plt.ylabel("Error at t = 5")
plt.yscale("log")
plt.xscale("log")
plt.legend(loc="best")
plt.title("Error of approximation at t = 5 with respect to delta t")
plt.show()

plt.figure()
plt.plot(time(COMMON_DELTA), error_precise(first, INFECTIONS),
         label="1st order error")
plt.plot(time(COMMON_DELTA),
         error_precise(second, INFECTIONS),
         label="2nd order error")
plt.xlabel("Time (days)")
plt.ylabel("Error")
plt.legend(loc="best")
plt.title(f"Error between order approximations and \
          exact growth (a = {INFECTIONS})")
