a=b=1
i=input()
i=int(i)
for n in range(1,i+1):
    print(a+b,end=' ')
    s=b+a
    a=b
    b=s
    