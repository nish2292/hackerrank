def Pcnt(lim):
    
    N1 = lim+1
    np = [0] * N1
    cnt = 0
    for i in range(2,N1):
        if np[i]==1:
            continue
        for f in range(i*2,N1,i):
            np[f] = 1
        cnt = cnt+1
    return cnt

mx = 41
F = [0] * 41
F[1] = 1
F[2] = 1
F[3] = 1
F[4] = 2
for i in range(5,mx):
    F[i] = F[i-1] + F[i-4]
    
T = input()

for t in range(T):
    N = input()
    print Pcnt(F[N])
