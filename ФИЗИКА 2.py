import numpy as np
import matplotlib.pyplot as plt
A = 1.0
omega = 2*np.pi
gamma = 0.1
t = np.linspace(0, 10, 5000)
x = A * np.exp(-gamma*t) * np.cos(omega*t)
v = ((-1 *A * np.e**(-1*gamma*t)) * (gamma* np.cos(omega*t) + omega*np.sin(omega*t)))
energy = 0.5 *v**2 * A
plt.figure(figsize=(12, 6))
plt.subplot(3, 1, 1)
plt.plot(t, x)
plt.xlabel('Время')
plt.ylabel('Амплитуда')
plt.grid()
plt.subplot(3, 1, 2)
plt.plot(t, energy)
plt.xlabel('Время')
plt.ylabel('Энергия')
plt.grid()
plt.subplot(3, 1, 3)
plt.plot(x, v)
plt.show()