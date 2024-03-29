from math import*
t=float(input('t='))
a=(2*t+1)
b=-3*t
c=t-6
dis=b**2-4*a*c
if(dis<0):
    print('при t=', t, 'уравнение не имеет действительных корней')
elif (a == 0):
    x=((t-6)/(3*t))
    print('при t=', t, 'уравнение имеет 1 действительный корень, равный', x)
else:
     x1= (-b + sqrt(dis))/(2*a)
     x2 = (-b - sqrt(dis))/(2*a)
     print('при t=', t,'уравнение имеет 2 действительных корня: x1=', x1, 'и x2=', x2)
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
ax.set_title('график зависимости дискриминанта от переменной t')
ax.set_xlabel('t')
ax.set_ylabel('дискриминант')
x=np.linspace(-10, 10,100)
y=(-3*x)**2-4*(2*x+1)*(x-6)
ax.plot(x, y)
plt.show()
