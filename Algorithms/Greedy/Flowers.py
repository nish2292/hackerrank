N,K = map(int,raw_input().strip().split())
A = map(int,raw_input().strip().split())
A.sort()
#print A

if K>=N:
    sm = sum(A)

else:
    i=N-1
    sm = 0
    X = 0 
    C = 0
    while i>=0:
        sm += A[i]*(X+1)
        C += 1
        if C>=K:
            X += 1
            C = 0
        i -= 1
print sm
