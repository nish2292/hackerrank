def ps(limit):
    N = limit+1
    NP = [0] * N
    psum = 0
    primes = []
    for i in range(2,N):
        if NP[i] == 1:
            primes.append(psum)
            continue
        for f in xrange(i*2,N,i):
            NP[f] = 1
        psum = psum + i
        primes.append(psum)
    return primes

T = input()
N = []
for t in range(T):
    N.append(input())

mxn = max(N)
ps1 = ps(mxn)
#print ps1
for t in range(T):    
    print ps1[N[t]-2]
