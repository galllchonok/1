#8 практика
import numpy as np
N = 3

A = np.genfromtxt('C:/Users/Даша/OneDrive/Рабочий стол/А-8.txt')
print('Исходный массив A')
print(A)

B = np.genfromtxt('C:/Users/Даша/OneDrive/Рабочий стол/Б-8.txt')
print('Исходный массив B')
print(B)
print('Обратная матрица A')
print(np.linalg.inv(A))

x = np.linalg.inv(A).dot(B)
print('')
print('X')
for i in range (0,N):
    print('%.3f'%x[i],end=' ')
print('')

x1 = np.linalg.solve(A,B)
print('')
print('X1')

for i in range (0,N):
    print('%.3f'%x1[i],end=' ')
print('')
print('\nDet(A)=%.3f'%np.linalg.det(A))