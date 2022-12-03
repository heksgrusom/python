#Y(x)=sin(10*x)*sin(3*x)/(x^2), x=[0...4]


import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,4)
y = np.sin(10*x)*np.sin(3*x)/(x**2)

plt.title("sin(10*x)*sin(3*x)/(x^2)", fontsize =15)
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x,y,label = 'sin(10*x)*sin(3*x)/(x^2)', color ="yellow", linewidth = 5)
plt.grid()


plt.show()