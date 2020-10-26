def my_func(a=1,b=0):
    x=3*a-b
    return x
print(my_func())
print(my_func(6))
print(my_func(3,5))
print(my_func(b=7))
print(my_func(b=3,a=0))