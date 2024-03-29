from math import*
import matplotlib.pyplot as pt
import numpy as np
m=0.01
A=0.2
w=(2*3.14)/3
t=np.linspace(0, 3,200)
x=A*np.cos(w*t)
r=-A*w*np.sin(w*t)
k=m*w**2
Ep=(1/2)*k*x**2
Ek=(1/2)*m*r**2
Epoln=Ep+Ek
fig, ax = pt.subplots()
ax.set_title('график зависимости Ек и Еп от t')
ax.set_xlabel('t')
ax.set_ylabel('Eп и Ек')
ax.plot(t, Ep*1000)
ax.plot(t, Ek*1000)
ax.plot(t, Epoln*1000)
ax.plot(t, x)
pt.show()
