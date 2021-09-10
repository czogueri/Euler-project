from matplotlib import pyplot
import numpy as np

x = np.linspace(0,4,40).round(2)

print(x)

y = [7]

r = 0

for k in x:
    p = k**2
    p = p.round(2)

    y.append(p)

    print(p)

    r = r + 1

    if k == x[38]:
        break

#print(y)

pyplot.plot(x,y)

pyplot.show()
