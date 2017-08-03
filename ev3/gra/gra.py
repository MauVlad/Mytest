import matplotlib.pyplot as plt
import numpy as np

plt.isinteractive()
False

plt.plot([1,2,3,4,5])

plt.show()

plt.ion()
plt.plot([1,2,3,4])

plt.ishold()
True

plt.plot(np.random.rand(10))
plt.plot(np.random.rand(10))
plt.show()

plt.figure('scatter')
plt.figure('plot')
a = np.random.rand(100)
b = np.random.rand(100)
plt.figure('scatter')
plt.scatter(a,b)
plt.figure('plot')
plt.plot(a,b)
