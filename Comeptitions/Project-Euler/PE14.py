def calc(i):
    
    if F[i]!=-1:
        return
    
    if i%2 == 0:
        T = i/2
    else:
        T = 3*i + 1
    if T>lim:
        F[i] = 1
        while T>lim:
            if T%2==0:
                T = T/2
            else:
                T = 3*T + 1
            F[i] = F[i] + 1
        calc(T)
        F[i] = F[i] + F[T]
    else:
        calc(T)
        F[i] = F[T] + 1

T = input()
N = [input() for i in range(T)]
lim = max(N)+1
F = [-1] * (lim+1)
ans = [-1] * (lim+1)
F[0] = 0
F[1] = 0
ans[0] = 0
ans[1] = 1
pos = 1
mx = 0
i = 1
for i in range(2,lim+1):
    calc(i)
    if(F[i]>=mx):
        #ans[i] = i
        pos = i
        mx = F[i]
    ans[i] = pos 
    
for i in range(T):
##    X = N[i]
##    A = F[0:X+1]
##    res = len(A)-1-A[::-1].index(max(A))
    print ans[N[i]]
