Mod = pow(10,9) + 7

def choose(n,k):
    py = [ [0]*(k+1) for _ in xrange(n+1) ]
    py[0][0] = 1
    for i in range(1,n+1):
        py[i][0] = 1
        L = min(i,k)
        for j in range(1,L+1):
            T1 = py[i-1][j]
            T2 = py[i-1][j-1]
            res = T1+T2
            py[i][j] = res % Mod
    return py

T = input()
N = []
M = []
for i in range(T):
    n,m = map(int, raw_input().strip().split())
    N.append(n)
    M.append(m)
    
nx = max(N)
mx = max(M)
NX = nx+mx
KX = max(nx,mx)
pyr = choose(NX,KX)
for i in range(T):
    print pyr[N[i]+M[i]][N[i]]
