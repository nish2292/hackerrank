# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def ppc(X, Y, N, mnX, mnY, svX, svY):
    arr = [(X[i] - mnX)*(Y[i] - mnY) for i in range(N)]
    if svX*svY*(N-1)!=0:
        res = sum(arr)/(N-1)/svX/svY
    else:
        res = -float("inf")
    return res
    
def stdev(A,mean,N):
    dev = [ (A[i]-mean)**2 for i in range(N) ]
    stddev = (sum(dev) + 0.0)/N
    stddev = math.sqrt(stddev)
    return stddev

T = input()
for t in range(T):
    N = input()
    G = map(float,raw_input().strip().split())
    mnG = sum(G)/N 
    dvG = stdev(G,mnG,N)
    #S = [[0.0 for j in range(N)] for i in range(5)]
    #mnS = [0.0 for j in range(5)]
    #dvS = [0.0 for j in range(5)]
    corr = [0.0 for j in range(5)]
    for i in range(5):
        T = map(float,raw_input().strip().split())
        S = [x+0.0 for x in T]
        mnS = (sum(T) + 0.0)/N 
        dvS = stdev(S,mnS,N)
        corr[i] = ppc(G,S,N,mnG,mnS,dvG,dvS)
    #print corr
    cr_max = max(corr)
    for i in range(5):
        if corr[i]==cr_max:
            print (i+1) 
            break
    
        
    
    
    
        
