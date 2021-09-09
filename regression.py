import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import plot


plt.gca().invert_yaxis()
plt.axis([-10, 10, -300, 300])

# curve functions
def line(x, b, m):
    return m*x + b

def cube(x, a, b, c, d):
    return a + b*x + c*x**2 + d*x**3

#generate original line
x = np.linspace(-7, 7, 80)
l1 = line(x, 12, .6)

#generate quad curve
c1 = cube(x, 2, 3, 1, 4)

#generate noise
noise_ctr = 0
noise_std = 20
noise = np.random.normal(noise_ctr,noise_std, len(x))

#noisy data
n_l1 = l1 + noise
n_c1 = c1 + noise

# fitcurve function
# def fit_curve(x, y, a, b):
#     n = len(x)
#     plot(x, line(x, a, b), color='k', alpha=.3)
#     for i in range(1000):
#         d1 = sum(a + b*x - y) * 2/n
#         d2 = sum((a + b*x - y)*x) * 2/n
#         a = a - .00005*d1
#         b = b - .00005*d2
#         if i % 2==0:
#             plot(x, line(x, a, b), color='k', alpha=.3)
#     plot(x, line(x, a, b))
#     return[a, b]

def cube_fit(x, y, a, b, c, d):
    n = len(x)
    plot(x, cube(x, a, b, c, d), color='k', alpha=.3)
    for i in range(4000):
        # h = a + bx + cx^2 + dx^3 + ex^4
        d1 = sum(a + b*x + c*x**2 + d*x**3 - y) * 2/n       #partial derivs
        d2 = sum((a + b*x + c*x**2 + d*x**3 - y)*x) * 2/n
        d3 = sum((a + b*x + c*x**2 + d*x**3 - y)*x**2) * 2/n
        d4 = sum((a + b*x + c*x**2 + d*x**3 - y)*x**3) * 2/n
        a = a - .0001*d1       #learning rates
        b = b - .00001*d2
        c = c - .00005*d3
        d = d - .000001*d4
        if i % 2 ==0:
            plot(x, cube(x, a, b, c, d), color='k', alpha=.3)
    plot(x, cube(x, a, b, c, d))
    return[a, b, c, d]

fit = cube_fit(x, n_c1, 5, 6, -10, -3)


# plotting things
# plot(x, n_curve, 'x')
# plot(x, l1, linewidth='1')
plot(x, c1, linewidth='1')
plot(x, n_c1, '.')
plot(x, cube(x, fit[0], fit[1], fit[2], fit[3]), color='blue')
plt.show()