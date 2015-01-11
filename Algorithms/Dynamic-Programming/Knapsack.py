T = input()

for t in range(T):
    N,M = map(int,raw_input().strip().split())
    A = map(int,raw_input().strip().split())
    res = [0]*(M+1)
    res[0] = 1
    for x in set(A):
        for i in range(x,M+1):
            res[i] = res[i] + res[i-x]
    #print res
    for i in range(0,M+1):
        if res[M-i]>0:
            print (M-i)
            break
