import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,101,0.2)
y1=np.sin(x)
y2=np.exp(x)
y3=np.cos(x)
y4=np.log(x)

ax1=plt.subplot(211)#(row,clos,index)هنا كده الرسمتين هيبقوا جمب بعض اكنهم عمودين
ax2=plt.subplot(212)


ax1.plot(x,y1)
ax2.plot(x,y2,'ro')
plt.figure()#open a single window 

plt.plot(x,y3)
plt.figure()

plt.plot(x,y4)


plt.tight_layout()#عشان تحسن التنسيق 
plt.show()