# regression_ver1.py (version 2)
# Max Kim
#
# Takes data and an expected trend. Generates a polynomial
# fit curve using gradient descent.

# import libraries
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import plot

# creates a cubic curve given a domain and coefficients.
def cube(x, a, b, c, d):
    return a + b*x + c*x**2 + d*x**3

# creates a fit curve using gradient descent.
# takes data arrays and guess coefficients, returns fit curve coefficient.
def fit_curve(x, y, a, b, c, d):
    n = len(x)
    plot(x, cube(x, a, b, c, d), color='k', alpha=.3)
    for i in range(350):
        # h = a + bx + cx^2 + dx^3
        d1 = sum(a + b*x + c*x**2 + d*x**3 - y) * 2/n       #partial derivs
        d2 = sum((a + b*x + c*x**2 + d*x**3 - y)*x) * 2/n
        d3 = sum((a + b*x + c*x**2 + d*x**3 - y)*x**2) * 2/n
        d4 = sum((a + b*x + c*x**2 + d*x**3 - y)*x**3) * 2/n
        a-= .001*d1       #learning rates
        b-= .001*d2
        c-= .001*d3
        d-= .00001*d4
        if i % 2 ==0:
            plot(x, cube(x, a, b, c, d), color='k', alpha=.3)
    plot(x, cube(x, a, b, c, d))
    return[a, b, c, d]


# generate axes
plt.axis([-10, 10, -300, 300])

#generate curve
x = np.linspace(-7, 7, 80)
c1 = cube(x, -2, 3, -5, -4)

#generate noise
noise_ctr = 0
noise_std = 20
noise = np.random.normal(noise_ctr, noise_std, len(x))

#noisy data
n_c1 = c1 + noise

# generate fit curve coefficients
fit = fit_curve(x, n_c1, 1, 1, 1, 1)

# plotting curves
plot(x, c1, linewidth='1')
plot(x, n_c1, '.')
plot(x, cube(x, fit[0], fit[1], fit[2], fit[3]), color='blue')
plt.show()