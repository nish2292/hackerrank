import math
A = raw_input()
N = len(A)

l = int(math.sqrt(N))
h = int(math.ceil(math.sqrt(N)))
if l*h<N:
    l= l+1

for i in range(h):
    res = ''
    for j in range(l):
        if(j*h+i)<N:
            res = res + A[j*h+i]
    print res,
