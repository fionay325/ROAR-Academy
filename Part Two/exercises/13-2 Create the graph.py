import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(1, 3, 100)

x1 = np.linspace(1,2, 100)
y1 = 2*x1

x = np.linspace(1,3, 100)

y = -3*x+10
plt.plot(x1, y1, color="blue")
plt.plot(x, y, color="blue")
plt.xlim(1,3)
plt.ylim(1,4)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Sample graph!")
plt.show()
