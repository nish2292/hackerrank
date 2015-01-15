N,M = map(int,raw_input().strip().split())
A = map(int,raw_input().strip().split())
B = map(int,raw_input().strip().split())
C = map(int,raw_input().strip().split())
Mod = pow(10,9) + 7
Mp = {}

for i in range(M):
    prev = 1
    if B[i] in Mp:
        prev = Mp[B[i]]
    Mp[B[i]] = (prev * C[i]) % Mod

for (b,c) in Mp.items():
    for i in xrange(b-1,N,b):
        A[i] = (A[i]*c) % Mod
    
for x in A:
    print x,
