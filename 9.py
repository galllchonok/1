import numpy as np

A=np.genfromtxt('C:/Users/Даша/OneDrive/Рабочий стол/AAA.txt')

print('Исходный массив A')
print(A)

B=np.genfromtxt('C:/Users/Даша/OneDrive/Рабочий стол/BBB.txt')
print('Исходный массив B')
print(B)

P=np.genfromtxt('C:/Users/Даша/OneDrive/Рабочий стол/PPP.txt')
print('Исходный массив P')
print(P)

Q=np.genfromtxt('C:/Users/Даша/OneDrive/Рабочий стол/QQQ.txt')
print('Исходный массив Q')
print(Q)

R=np.genfromtxt('C:/Users/Даша/OneDrive/Рабочий стол/RRR.txt')
print('Исходный массив R')
print(R)

x = np.dot(A,Q)
print ('x =', x)

y = np.dot(A,x)
print ('y =', y)

z = x+y
print ('z =', z)
s = np.dot(z,Q)
print ('s =', s)