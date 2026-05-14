import numpy as np
import matplotlib.pyplot as plt

x=np.arange(-100,101,1)
y=0.5*x**2+2*x

plt.plot(x,y,'y--')

y1=np.sin(x)

plt.plot(x,y1,'g')

y2=np.cos(x)

plt.plot(x,y2,'b')
plt.show()