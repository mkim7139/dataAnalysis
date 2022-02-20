# regression_ver2.py (version 2)
# Max Kim
#
# Takes data and an expected trend (linear, quadratic, cubic,...)
# Generates a polynomial fit curve using gradient descent.

# import libraries
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import plot

# import powerRule_ver3 file to calculate derivatives
from powerRule_ver3 import *
derive('x^3 -1x^(-4)', 2)

def polynomial(x, coefs):
    coefs=coefs.astype('float64')
    func=0
    for i in range(len(coefs)):
        func+=coefs[i] * (x**i)
    return func

# creates a fit curve using gradient descent.
# takes data arrays and guess coefficients, returns fit curve coefficient.
def fit_curve(x, y, coefs):
    coefs=coefs.astype('float64')
    n = len(x)
    plot(x, polynomial(x, coefs), color='g', alpha=.5)
    for i in range(900):
        # error = (a + bx + cx^2 + dx^3)^2 / n
        d1 = sum(coefs[0] + coefs[1]*x + coefs[2]*x**2 + coefs[3]*x**3 - y) * 2/n       #partial derivs
        d2 = sum((coefs[0] + coefs[1]*x + coefs[2]*x**2 + coefs[3]*x**3 - y)*x) * 2/n
        d3 = sum((coefs[0] + coefs[1]*x + coefs[2]*x**2 + coefs[3]*x**3 - y)*x**2) * 2/n
        d4 = sum((coefs[0] + coefs[1]*x + coefs[2]*x**2 + coefs[3]*x**3 - y)*x**3) * 2/n

        coefs[0]-= .001*d1       #learning rates
        coefs[1]-= .0001*d2
        coefs[2]-= .0001*d3
        coefs[3]-= .00001*d4
        if i % 2 ==0:
            plot(x, polynomial(x, coefs), color='k', alpha=.3)
    plot(x, polynomial(x, coefs))
    return coefs


# generate axes
plt.axis([-10, 10, -300, 300])

#generate curve
x = np.linspace(-7, 7, 80)
c1_coefs=np.array([-2, 3, -5, -4])
c1 = polynomial(x, c1_coefs)

#generate noise
noise_ctr = 0
noise_std = 20
noise = np.random.normal(noise_ctr, noise_std, len(x))

#noisy data
n_c1 = c1 + noise

# generate fit curve coefficients
starting_coefs=np.array([1, 1, 1, 1])
fit_coefs = fit_curve(x, n_c1, starting_coefs)


# plotting curves
plot(x, c1, linewidth='1')
plot(x, n_c1, '.')
plot(x, polynomial(x, fit_coefs), color='blue')
plt.show()
