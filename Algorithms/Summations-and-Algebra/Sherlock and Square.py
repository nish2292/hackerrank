import math


T = input()
n = []

for t in range(T):
    N =input()
    n.append(N)
    
for t in range(T):   
    temp = 1
    #while (N+1)!=0:
    #    temp = (temp << 1)% 1000000007
    #    N = N-1
    temp = int(pow(2,n[t]+1,1000000007))
    sum = (2 + temp)
    print sum
