import math
import matplotlib.pyplot as plt


def cos_approx(delta):
    """
    Approximates the cosine curve based on finite difference approximation with delta

    Parameters
    ----------
    delta : float
        Step size used for approximation
    """
    t = 0
    x = []
    y = []
    while(t + delta <= 2 * math.pi):
        x.append(t)
        y.append((math.sin(t + delta) - math.sin(t))/delta)
        t += delta
    plt.plot(x, y)
    plt.show()


def first_approx(y0, delta, alpha, numdays):
    """
    Approximates the number of people infected with covid-19 based on first-order approximation

    Parameters
    ----------
    y0 : int
        Number of people infected at start
    delta : float
        Step size for change in time
    alpha : int
        Number of people that infected person passes disease to
    numdays : int
        Number of days of approximation

    Returns
    -------
    x : list of floats
        List of people infected from start to numdays in increments of delta
    float
        Number of days actually calculated in this first-order approximation
    """
    x = [y0]
    i = delta
    while i <= numdays:
        x.append((1 + alpha * delta) * x[-1])
        i += delta
    return x, i-delta


def second_approx(y0, delta, alpha, numdays):
    """
    Approximates the number of people infected with covid-19 based on second-order approximation

    Parameters
    ----------
    y0 : int
        Number of people infected at start
    delta : float
        Step size for change in time
    alpha : int
        Number of people that infected person passes disease to
    numdays : int
        Number of days of approximation

    Returns
    -------
    x : list of floats
        List of people infected from start to numdays in increments of delta
    float
        Number of days actually calculated in this second-order approximation
    """
    x = [y0]
    i = delta
    multiplier = (1 + alpha * delta/2) / (1 - alpha * delta/2)
    while i <= numdays:
        x.append(multiplier * x[-1])
        i += delta
    return x, i-delta


def return_t(delta, numdays):
    """
    Gives timestamps for each delta increment of numdays

    Parameters
    ----------
    delta : float
        Step size for change in time
    numdays : int
        Number of days

    Returns
    -------
    list of floats
        Timestamps of all delta increments of numdays
    """
    return [delta * i for i in range(0, int((numdays)/delta))]

alpha = 1.2
numdays = 5
y0 = 1

dt = []
first_error = []
second_error = []
delta = 0.01

while delta <= 0.5:
    first, time1 = first_approx(y0, delta, alpha, numdays)
    second, time2 = second_approx(y0, delta, alpha, numdays)
    first_error.append(abs(math.exp(alpha * time1) - first[-1]))
    second_error.append(abs(math.exp(alpha * time2) - second[-1]))
    dt.append(delta)
    delta += 0.01

plt.xlabel('delta')
plt.ylabel('error in covid cases')
plt.xscale('log')
plt.yscale('log')
plt.plot(dt, first_error, 'r--')
plt.plot(dt, second_error, 'bs')
plt.show()
