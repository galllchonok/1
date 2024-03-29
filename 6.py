import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-5, 5,100)
y=x**(4)-2*x**(3)-3*x**(2)+4*x-1
fmax= max(y)
fmin= min(y)
print(fmin, fmax)
fig, ax = plt.subplots()
ax.set_title('график функции')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.plot(x, y)
plt.show()
