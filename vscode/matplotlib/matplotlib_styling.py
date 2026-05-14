import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style



x=np.arange(0,200,0.2)
y=np.sin(x)
y2=np.cos(x)

plt.title('sine function')
plt.suptitle('1st day')

plt.xlabel('random')
plt.ylabel('sine fun')
plt.grid(True)

plt.plot(x,y,label='sine')
plt.plot(x,y2,label='cos')

plt.legend(loc='upper left')#lower left and right also

plt.show()