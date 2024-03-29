f = open('C:/Users/Даша/OneDrive/Рабочий стол/6-7.txt', 'r')
line = f.read()
X = []
for x in line.split():
    X.append(int(x))
print('Исходный массив X')
print(X)
N=len(X)
c=0
s=0
d=-1
y=X.index(d)
for i in range(N):
    if X[i]>=0:
        X[i] *=0
    else:
        if X[i]<0:
            s+=1
print('Новый массив Х')
print(X)
while 0 in X:
    X.remove(0)
c=max(X)
print('кол-во отрицательных элементов в массиве ', s, ',максимальный отрицательный элемент', c, ',его номер в массиве', y)
f.close()
