a=float(input('a='))
b=float(input('b= '))
c=float(input('c='))
if a + b <= c or a + c <= b or b + c <= a:
    print('Треугольник не существуе')
elif a != b and a != c and b != c:
    print('Треугольник существует')
elif a == b == c:
    print('Равносторонний')
else:
    print('Равнобедренный')
