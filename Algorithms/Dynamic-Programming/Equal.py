T = input()

for t in range(T):
    N = input()  
    A = map(int, raw_input().strip().split())
    if N<2:
        print '0'
        continue

    mv = min(A)

    mc = 1000000007
    for i in range(6):
        c=0
        for j in range(N):
            V = A[j] - mv + i;
            c = c + int(V/5)
            V = V % 5
            c = c + int(V/2)
            c = c + (V&1)
        if c<mc:
            mc = c
    print mc
