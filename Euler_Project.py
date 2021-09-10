import numpy as np
import sympy as sp
from scipy.misc import derivative

from matplotlib import pyplot


x = np.linspace(0,4,40).round(1)

print(x)

y = []

r = 0

y.append(1)

for u in x:
    v = sp.exp(2 * u) * 0.1 + y[r]

    v = v.round(2)

    r = r + 1

    print(v)
    y.append(v)

     # if u == x[38]:
     #    break

print(len(y))


pyplot.plot(x,y,)


pyplot.show()










