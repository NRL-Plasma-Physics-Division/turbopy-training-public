"""
Approximates differential equations  numerically.

The program calculates cosine as the derivative of sine.
It then approximates exponential growth with first and second order approximations.
"""

import math
import matplotlib.pyplot as plt
import numpy as np

def approx_cos(delta):
    """
    Approximates the value of cosine as the derivative of sine.

    Parameters
    ----------
    delta : float
        Defines the size of the step in time each step of the program

    Returns
    -------
    xsteps : list of float
        A list of each time value for which the expression was evaluated
    ysteps : list of float
        A list of the value of cosine at each t in `xsteps`
    """
    xsteps = [0]
    ysteps = [1]
    t = 0
    while t < 2*math.pi:
        y = math.sin(t+delta)
        y -= math.sin(t)
        y /= delta
        t += delta/2
        xsteps.append(t)
        ysteps.append(y)
    return xsteps, ysteps

def cos_plot():
    """
    Plots approximates cosine graphs as described in `approxCos`.
    For comparison, it also graphs a true cosine wave.
    """
    plt.plot(*approx_cos(1), label="delta = 1")
    plt.plot(*approx_cos(1/2), label="delta = 1/2")
    plt.plot(*approx_cos(1/3), label="delta = 1/3")

    tsteps = np.arange(0, 2*np.pi, .1)
    plt.plot(tsteps, np.cos(tsteps), label="Actual cosine")

    plt.xlabel("Time")
    plt.ylabel("Cosine")
    plt.title("Approximate cosine plots with finite differences")

    plt.legend()
    plt.show()

def first_order_disease(alpha, delta):
    """
    Calculates exponential growth with a first order approximation.

    Parameters
    ----------
    alpha : float
        The factor for growth rate, i.e. the static exponential term
    delta : float
        The step size in time for each evaluation of the expression

    Returns
    -------
    tsteps : list of float
        A list of all the times for which the approximation was evaluated
    ysteps : list of float
        A list of all the values of the approximation, corresponding to `tsteps`
    """
    y = 1
    t = 0
    tsteps = [0]
    ysteps = [1]
    while t + delta < 5:
        y = (1 + alpha*delta)*y
        t += delta
        tsteps.append(t)
        ysteps.append(y)
    return tsteps, ysteps

def second_order_disease(alpha, delta):
    """
    Calculates exponential growth with a second order approximation

    Differs from `first_order_disease` in implementation, but accepts and returns similar arguments

    Parameters
    ----------
    alpha : float
        The growth rate factor, static exponential term
    delta : float
        The step size in time for each evaulation of the approximation

    Returns
    -------
    tsteps : list of float
        List of all the values for time at which the approximation was evaluated
    ysteps : list of float
        List of the values of the approximation at each evaluation
    """
    y = 1
    t = 0
    tsteps = [0]
    ysteps = [1]
    while t+delta < 5:
        difference = alpha*delta/2
        factor = (1+difference)/(1-difference)
        y *= factor
        t += delta
        tsteps.append(t)
        ysteps.append(y)
    return tsteps, ysteps

def disease_error(alpha, delta):
    """
    Calculates the error between the approximated and true exponential growth

    Uses both `first_order_disease` and `second_order_disease`

    Parameters
    ----------
    alpha : float
        Rate of growth for the exponential, the static term in the power
    delta : float
        The step size in time at which the approximations and real value are evaluated

    Returns
    -------
    time1 : list of float
        The list of time-values returned by `first_order_disease`
    first_error : list of float
        The difference between the first-order approximation
        and real exponential value for each t in `time1`
    time2 : list of float
        The list of time-values returned by `second_order_disease`, should be identical to `time1`
    second_error : list of float
        The difference between the second-order approximation
        and real exponential value for each t in `time2`
    """
    time1, cases1 = first_order_disease(alpha, delta)
    time2, cases2 = second_order_disease(alpha, delta)
    first_error = []
    second_error = []
    for t in time1:
        sim_cases = cases1[time1.index(t)]
        error = abs(pow(math.e, alpha*t) - sim_cases)
        first_error.append(error)
    for t in time2:
        sim_cases = cases2[time2.index(t)]
        error = abs(pow(math.e, alpha*t) - sim_cases)
        second_error.append(error)
    return time1, first_error, time2, second_error

def first_order_final_error(alpha, delta):
    """
    Returns the error of the last value in the first order exponential approximation

    Parameters
    ----------
    alpha : float
        The factor for growth rate, i.e. the static exponential term
    delta : float
        The step size in time for each evaluation of the expression

    Returns
    -------
    margin : float
        The difference between the real exponential value and first-order approximation.
        Calculated at the highest value of time less than five
    """
    t = 0
    y = 1
    while t < 5:
        y = (1 + alpha*delta)*y
        t += delta
    margin = abs(y - pow(math.e, alpha*t))
    return margin

def second_order_final_error(alpha, delta):
    """
    Returns the error of the last value in the second order exponential approximation

    Parameters
    ----------
    alpha : float
        The factor for growth rate, i.e. the static exponential term
    delta : float
        The step size in time for each evaluation of the expression.

    Returns
    -------
    margin : float
        The difference between the actual exponential and the second-order approximation.
        Calculated at the highest value of time less than five
    """
    y = 1
    t = 0
    while t < 5:
        difference = alpha*delta/2
        y = y*(1+difference)/(1-difference)
        t += delta
    margin = abs(y - pow(math.e, alpha*t))
    return margin

def delta_error(alpha):
    """
    Finds the errors of the last values of both first and second order approximations.

    Each approximation is evaluated for many deltas(see above) between zero and one.

    Parameters
    ----------
    alpha : float
        The static rate of growth, i.e. the static exponential term

    Returns
    -------
    deltas : list of floats
        List of all the step sizes the approximations were evaluated with
    first_errors : list of floats
        List of final errors (`first_order_final_error`)
        found by first-order approximation for each delta
    second_errors : list of floats
        List of final errors (`second_order_final_error`)
        found by second-order approximation for each delta
    """
    deltas = np.arange(.01, 1, .005)
    first_errors = []
    second_errors = []
    for d in deltas:
        first_errors.append(first_order_final_error(alpha, d))
        second_errors.append(second_order_final_error(alpha, d))
    return deltas, first_errors, second_errors

def disease_plot(alpha, delta):
    """
    Creates a plot of the two approximations of exponential growth.

    For comparison, also shown is a real exponential growth line

    Parameters
    ----------
    alpha : float
        The factor for growth rate, i.e. the static exponential term
    delta : float
        The step size in time for each evaluation of the expression
    """
    plt.plot(*first_order_disease(alpha, delta), label="First Order Approximation")
    plt.plot(*second_order_disease(alpha, delta), label="Second Order Approximation")

    tsteps = np.arange(0, 5, .1)
    plt.plot(tsteps, np.exp(tsteps*alpha), label="Actual Cases")

    plt.xlabel("Time (days)")
    plt.ylabel("Cases")
    plt.title("Approximating cases of a disease")

    plt.legend()
    plt.show()

def error_plot(alpha, delta):
    """
    Plots the error between approximations and real exponential growth.

    Both first-order and second-order error is plotted

    Parameters
    ----------
    alpha : float
        The factor for growth rate, i.e. the static exponential term
    delta : float
        The step size in time for each evaluation of the expression
    """
    time1, first_error, time2, second_error = disease_error(alpha, delta)
    plt.plot(time1, first_error, label="First Order Error")
    plt.plot(time2, second_error, label="Second Order Error")

    plt.xlabel("Time (days)")
    plt.ylabel("Absolute Error")
    plt.title("Error in first- and second-order approximations of disease cases.")

    plt.legend()
    plt.show()

def delta_plot():
    """
    Plots error as a function of delta.

    Both first and second-order errors are shown.
    Alpha equals one for all approximations and evaluations referenced
    """
    delta_steps, first_error, second_error = delta_error(1)
    plt.loglog(delta_steps, first_error, label="First Order Error")
    plt.loglog(delta_steps, second_error, label="Second Order Error")

    plt.xlabel("Delta-T")
    plt.ylabel("Error")
    plt.title("Error in first- and second-order exponential approximations (log plot)")
    plt.grid(True)

    plt.legend()
    plt.show()

cos_plot()

TRANSMISSION = float(input("How many new cases per infected per day? "))
FREQUENCY = 1/float(input("How many times a day should we evaluate the model? "))

disease_plot(TRANSMISSION, FREQUENCY)
error_plot(TRANSMISSION, FREQUENCY)
delta_plot()
