from matplotlib import pyplot
import numpy as np

# a range of indices from 0 to 39
krange = np.array(range(40))
# adjustable step in x direction
dx = 0.1
# the range of x values
x = dx*krange
# make an array for the solution, all zeros for now
y = np.zeros(len(krange))
#
# we want to find a solution for the ODE dy/dx = -2*y
# with the initial value y(0) = 2.
# by using the Euler method, which means to iterate recursively
# y_k+1 = y_k + dx*y' = y_k - 2*dx*y_k = y_k * (1 - 2*dx)
#
y[0] = 2.0

for k in krange:
# avoid the out of range error
	if(k == krange[-1]) : break
	y[k+1] = y[k]*(1 - 2*dx)

# calculate the exact solution (for this case is trivial)
y_sol = 2*np.exp(-2*x)
# and compare it to the numerical solution in the same graph
pyplot.plot(x,y, x, y_sol)
pyplot.show()