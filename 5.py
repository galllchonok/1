x=int(input('x='))
y=int(input('y='))
z=int(input('z='))
print('x+y=',x+y, 'x*y=',x*y)
print('x=',x, 'y*z=',y*z)
if (x+y)<(x*y) and (x< y*z):
    print((x+y)/(y*z))
elif (x+y)>(x*y) and (x< y*z):
    print((x*y) / (y * z))
elif (x+y)<(x*y) and (x> y*z):
    print((x+y)/x)
elif (x+y)>(x*y) and (x> y*z):
    print((x*y)/x)


