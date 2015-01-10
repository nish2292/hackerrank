T = input()

for t in range(T):
    N = input()
    n=N
    res = -1
    for a in range(2,N):
        num = N*(N-2*a)
        den = 2*n - 2*a
        if num%den == 0:
            b = num/den
            c = n-a-b
            if b>0 and c>0:
                prod = a*b*c
                #print a,b,c,prod
                res = max(res,prod)
    print res
