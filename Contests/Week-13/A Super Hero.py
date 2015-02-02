T = input()

for t in range(T):
    N,M = map(int,raw_input().strip().split())
    P = []
    for i in range(N):
        T3 = map(int,raw_input().strip().split())
        P.append(T3)
    B = []
    for i in range(N):
        T3 = map(int,raw_input().strip().split())
        B.append(T3)
    i = N-1
    cst = [0] * M
    T2 = [P[i][j] for j in range(M)]
    while i > 0:
        res2 = []
        k = 0 
        while k<M:
        #for k in range(M):
            k2 = 0 
            while k2<M:
            #for k2 in range(M):
                if k2==0:
                    res = P[i][k2] - B[i-1][k] 
                    res = max(res,0)
                    res = res + cst[k2]
                else:
                    tp = P[i][k2] - B[i-1][k]
                    tp = max(tp,0)
                    tp = tp + cst[k2]
                    res = min(tp,res)
                k2=k2+1
                if res==0:
                    break
                
            res2.append(res)
            k = k + 1
        #print res2
        cst = res2
        i=i-1
    
    i=0
    while i<M:
        if i==0:
            mn = P[0][i]+cst[i]
        else:
            mn = min(mn,P[0][i]+cst[i])
        i = i + 1
    print mn
