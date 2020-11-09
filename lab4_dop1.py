a=input('a=')
a=int(a)
n=input('n=')
n=float(n)
def my(a,n):
    if n==0:
        return 1
    x=my(a*a,n//2)
    if n%2:
        x*=a
    return x
print(my(a,n))
