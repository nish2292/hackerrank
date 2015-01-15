T =input()
for t in range(T):
    N=input()
    A=map(int,raw_input().strip().split())
    res1 = 0
    res2 = 0
    res1 = A[0]^A[N-1]
    for i in range(1,(N-1)):
        if i%2==0:
            res1 = res1^A[i]
    if N%2==0:
        print '0'
    else:
        print res1
