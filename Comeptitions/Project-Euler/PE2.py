def fibs(n):
    a=1
    b=1
    d=0
    c=a+b
    while c<=n:
        if c%2 == 0:
            d+=c
        a=b
        b=c
        c=a+b
    return d

T=input()
for t in range(T):
    n=input()
    res = fibs(n)    
    print res
