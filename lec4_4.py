def my(a,b):
    x1=3*a+2*b
    x2=5*b-3*a
    return x1,x2
a=my(3,2)
print(type(a))
print(a[0])
print(a[1])
print(my(3,2)[1])