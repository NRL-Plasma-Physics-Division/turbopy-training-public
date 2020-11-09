import matplotlib.pyplot as plt
import numpy as np
import sys
# command line: python tang.py {alpha} {dt (step size)}
if not sys.argv[1:]:
    print('please input an alpha and dt value')
    exit()
ALPHA = float(sys.argv[1])
DT = float(sys.argv[2])


def firstorder(y0, n, dt):
    """
    Calculates a list of first-order approximations
    
    Parameters
    ----------
    y0 : float
        Initial y value
    n : int
        Number of days calculated for
    dt : float
        Step size of t
    
    Returns
    --------
    f : list of float
        List of first-order approximations from t = 0 to t = n
    """
    
    i = dt
    f = [y0]
    while i <= n:
        f += [(1 + (ALPHA * dt)) * f[-1]]
        i += dt
    return f


def secondorder(y0, n, dt):
    """
    Calculates a list of second-order approximations

    Parameters
    ----------
    y0 : float
        Initial y value
    n : int
        Number of days calculated for
    dt : float
        Step size of t

    Returns
    --------
    s : list of float
        List of second-order approximations from t = 0 to t = n
    float
        final value for t
    """
    
    i = dt
    s = [y0]
    while i <= n:
        s += [s[-1] * (1 + ALPHA * dt / 2) / (1 - ALPHA * dt / 2)]
        i += dt
    return s, i-dt


dt = np.arange(0.0, 5.0 + DT, DT)
t = np.arange(0.0, 5.01, 0.01)
control = np.exp(t * ALPHA)

fig1, one = plt.subplots()
one.plot(dt, firstorder(1, 5, DT), label='first order')
one.plot(dt, secondorder(1, 5, DT)[0], label='second order')
one.plot(t, control, label='exact')
one.set(xlabel='time (days)', ylabel='covid cases', title='first & second approximations')
one.grid()
one.legend()

ALPHA, DT = 1, 1
dt = np.arange(0.0, 5.0 + DT, DT)
control = np.exp(dt * ALPHA)
first = firstorder(1, 5, DT)
second = secondorder(1, 5, DT)[0]

fig2, two = plt.subplots()
two.plot(dt, np.abs(control - first), label='first order error')
two.plot(dt, np.abs(control - second), label='second order error')
two.set(xlabel='time (days)', ylabel='error', title='first & second approximation errors')
two.grid()
two.legend()

DT = 0.01
dt_values = np.logspace(-3, 0, 100)
control = np.exp(5)
first = [firstorder(1, 5, d)[-1] - control for d in dt_values]
second = []
for d in dt_values:
    sec, i = secondorder(1, 5, d)
    second += [sec[-1] * (1 + ALPHA * (5 - i) / 2) / (1 - ALPHA * (5 - i) / 2) - control]

fig3, three = plt.subplots()
three.set_xscale('log')
three.set_yscale('log')
three.plot(dt_values, np.abs(first), label='first order error')
three.plot(dt_values, np.abs(second), label='second order error')
three.set(xlabel='time (days)', ylabel='error', title='first & second approximation errors log log')
three.grid()
three.legend()

fig4, four = plt.subplots()
four.plot(np.arange(0.0, 2*np.pi, 1/2), np.cos(np.arange(0.0, 2*np.pi, 1/2)), label='delta = 1')
four.plot(np.arange(0.0, 2*np.pi, 1/4), np.cos(np.arange(0.0, 2*np.pi, 1/4)), label='delta = 1/2')
four.plot(np.arange(0.0, 2*np.pi, 1/6), np.cos(np.arange(0.0, 2*np.pi, 1/6)), label='delta = 1/3')
four.plot(np.arange(0.0, 2*np.pi, 0.01), np.cos(np.arange(0.0, 2*np.pi, 0.01)), label='cosine')
four.set(xlabel='x', ylabel='y', title='cosine approximations')
four.legend()
plt.show()
