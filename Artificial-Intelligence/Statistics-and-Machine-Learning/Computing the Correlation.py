# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
N = input()
M = []
P = []
C = []
for i in range(N):
    m,p,c = map(int,raw_input().strip().split())
    M.append(m)
    P.append(p)
    C.append(c)
mu_m = sum(M) / N
mu_p = sum(P) / N
mu_c = sum(C) / N
res1 = 0.0
res2 = 0.0
res3 = 0.0
sm , sp, sc = 0.0,0.0,0.0
for i in range(N):
    dm = M[i] - mu_m
    dp = P[i] - mu_p
    dc = C[i] - mu_c
    res1 += dm * dp
    res2 += dc * dp
    res3 += dm * dc
    sm += dm**2
    sp += dp**2
    sc += dc**2
    
sm = math.sqrt(sm/(N-1))
sp = math.sqrt(sp/(N-1))
sc = math.sqrt(sc/(N-1))
    
res1 = res1 / (N-1) / sm / sp
res2 = res2 / (N-1) / sc / sp
res3 = res3 / (N-1) / sm / sc

print ("%.2f" % res1)
print ("%.2f" % res2)
print ("%.2f" % res3)
