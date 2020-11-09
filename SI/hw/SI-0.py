"""Program to estimate the derivatives of sinusoidal and exponential functions

"""

import math
import matplotlib.pyplot as plt
import numpy as np

def est_cos(delta_t):
    r"""Estimates a cosine graph as the derivative of a sine graph
    
    Takes in a time step 'delta_t' and uses that to generate `time` a
    variable representing time which is a list of all the time values
    used in the derivative calculation. Also generates `est`, a list of
    all the calculated cosine function values. On a graph, `time` will be
    on the x-axis and `est` will be on the y-axis
    
    Parameters
    ----------
    delta_t : float or int
        Time step for estimating the derivative. Used to generate local variable
        'time' represeting time, which will end up being the x-axis values on the
        cosine graph.
    
    Returns
    -------
    time : numpy.ndarray
        Time values used for differentiation
    est : numpy.ndarray
        Differentiation estimates
    """
    time = np.arange(0, 2*math.pi, delta_t/2)
    est = []
    for i in time:
        est.append((np.sin(i+delta_t/2)-np.sin(i-delta_t/2))/delta_t)
    return time, np.array(est)

def show_cos():
    r"""Displays the cosine approximations in a graph
    
    This method takes in not arguments and does not return anything. It runs the
    est_cos method three times with a time step of 1, 1/2, and 1/3, and plots the
    values the method returns. It also plots a real cosine graph for comparison.
    """
    cos_t = np.arange(0, 2*math.pi, 0.05)
    plt.plot(*est_cos(1), 'r-',
             *est_cos(1/2), 'b-',
             *est_cos(1/3), 'g-',
             cos_t, np.cos(cos_t), 'k-')
    plt.figlegend(('Delta t = 1', 'Delta t = 1/2', 'Delta t = 1/3', 'Cosine'))
    plt.show()

def est_covid_first_order(alpha, delta_t):
    r"""Estimates the covid infections using first order estimation
    
    Takes in a value for `alpha`, the growth factor, and `delta_t`, the time step.
    Generates `time`, a list of time values which will be on the x-axis of the plot,
    and `est`, which will be plotted on the y-axis. `est` is found using first
    order estimation.
    
    Parameters
    ----------
    alpha : float or int
        Average number of people an infected person will infect per day, used
        in first order estimation.
    delta_t : float or int
        Time step used in first order estimation. Also used to generate 'time'.
    
    Returns
    -------
    time : numpy.ndarray
        Time values used for estimation
    est : numpy.ndarray
        First order estimation values
    """
    time = np.arange(0, 5.01, delta_t)
    est = [1]
    for i in range(1, len(time)):
        est.append((1+alpha*delta_t)**i)
    return time, np.array(est)

def est_covid_second_order(alpha, delta_t):
    r"""Estimates the covid infections using second order estimation
    
    Takes in a value for `alpha`, the growth factor, and `delta_t`, the time step.
    Generates `time`, a list of time values which will be on the x-axis of the plot,
    `est`, which will be plotted on the y-axis, and `coef`, which is used to
    generate `est`. `est` is found using second order estimation.
    
    Parameters
    ----------
    alpha : float or int
        Average number of people an infected person will infect per day, used
        in second order estimation.
    delta_t : float or int
        Time step used in second order estimation. Also used to generate 'time'.
    
    Returns
    -------
    time : numpy.ndarray
        Time values used for estimation
    est : numpy.ndarray
        Second order estimation values
    """
    time = np.arange(0, 5.01, delta_t)
    est = [1]
    coef = alpha*delta_t/2
    for i in range(1, len(time)):
        est.append(((1+coef)/(1-coef))**i)
    return time, np.array(est)

def show_covid(alpha, delta_t):
    r"""Displays the results of the above estimations on a plot.
    
    Takes in a value for `alpha`, the growth factor, and `delta_t`, the time step.
    Runs est_covid_first_order and est_covid_second_order with those arguments and
    plots their results. Also gerates and plots the true results of the covid
    spread problem for comparison. This method does not return anything.
    
    Parameters
    ----------
    alpha : float or int
        Average number of people an infected person will infect per day.
    delta_t : float or int
        Time step used in estimations and true results
    """
    real_t = np.arange(0, 5.01, 0.05)
    real_covid = math.e**(1*real_t)
    plt.plot(*est_covid_first_order(alpha, delta_t), 'r-',
             *est_covid_second_order(alpha, delta_t), 'b-',
             real_t, real_covid, 'k-')
    plt.figlegend(('First Order', 'Second Order', 'Actual'))
    plt.xlabel('Time (days)')
    plt.ylabel('Cases')
    plt.show()

def covid_error():
    r"""Calculates the error of the of the above estimates
    
    This function takes in no arguments. Generates `time`, a list of times with
    logarithmic increments, `est1`, the errors for first order approximation,
    and `est2`, the errors for second order approximation. `est1` and `est2`
    are generated from calling est_covid_first_order and est_covid_second_order
    respectively, each with arguments alpha = 1 and delta_t = the next value
    in `time`.
    
    Returns
    -------
    time
        List of logarithmic time values used in estimation
    est1
        List of error values for first order approximation
    est 2
        List of error values for second order approximation
    """
    time = []
    est1 = []
    est2 = []
    real = math.e**(5)
    for i in range(5):
        exp = (1/2)**(i+1)
        time.append(exp)
        est1.append(abs(est_covid_first_order(1, exp)[1][-1]-real))
        est2.append(abs(est_covid_second_order(1, exp)[1][-1]-real))
    return time, est1, est2

def show_covid_error():
    """Displays the results of covid_error() on a log-log plot
    
    This function takes in no arguments. Calls covid_error and from that gerates
    `time` a list of time values, `errfirst`, the errors for first order estimation,
    and `errsecond`, the errors for second order estimation. Plots both `errfirst`
    and `errsecond` with 'time' on the x-axis. This function returns nothing
    """
    time = covid_error()[0]
    errfirst = covid_error()[1]
    errsecond = covid_error()[2]
    plt.loglog(time, errfirst, 'b-', time, errsecond, 'r-')
    plt.figlegend(('First Order', 'Second Order'))
    plt.xlabel('Delta t (days)')
    plt.ylabel('Error (cases)')
    plt.show()

show_cos()
ALPHA = 1
DELTA_T = 1
show_covid(ALPHA, DELTA_T)
show_covid_error()
