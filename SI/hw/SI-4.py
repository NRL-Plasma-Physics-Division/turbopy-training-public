import numpy as np
import matplotlib.pyplot as plt

# Did this a few weeks ago, so it may not line up perfectly with the prompt

### Finite difference of Sinx ###
def ddt_sin(t, delta_t):
    """derivative of sine using finite difference theorem
    inputs:
    - t = what the term is a function of; can be y, x, etc.
    - delta_t = the small but finite term
    Returns: dy/dt = [y(t+delta_t) - y(t)]/delta_t
    """
    return (np.sin(t+delta_t) - np.sin(t))/delta_t

t = 0 # initial time
t_tot = np.arange(0.01, 3.1415*2, 0.01) # total of 2pi
der_sine = np.zeros(len(t_tot)) # the derivative of sin(x) is cos(x)
for i in range(len(t_tot)):
    der_sine[i] = ddt_sin(t, delta_t=0.01)
    t = t_tot[i] # sets the next time t

cosine = np.cos(t_tot) # testing to see if our finite difference works

plt.figure(1, figsize=(8,8))
plt.plot(t_tot, der_sine, 'k-.', label='finite diff')
plt.plot(t_tot, cosine, 'y--', label='actual')
plt.legend()
plt.title('Finite difference of sin(x)')
plt.show()

### Covid Problem ###
def y_t_dt(yt, dt, alpha):
    """This is for dy/dt = alpha*y"""
    return yt*(alpha*dt + 1)

t_total = np.arange(0.01, 1.01, 0.01) # total time of 1, starting at 0.01
alpha = 2 # people who get infected
y_t = 1 # initial value of people infected at t=0
y_n = np.zeros(len(t_total)) # initialize array
dt = 0.01

for i in range(len(t_total)): # looping through total time
    y_t = y_t_dt(y_t, dt, alpha) # uses previous y(t) to find the next y(t)
    y_n[i] = y_t

# if you solve the differential equation, you get y(t) = e^(alpha*t)
y_exp = 1 * np.exp(alpha*t_total)

plt.figure(2, figsize=(8,8))
plt.plot(t_total, y_n, 'k-.', label='finite diff')
plt.plot(t_total, y_exp, 'y--', label='actual')
plt.legend()
plt.title('Exponential growth of an infection')
plt.show()


