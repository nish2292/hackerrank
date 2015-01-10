T = input()

for t in range(T):
    N,K = map(int,raw_input().strip().split())
    A = raw_input()
    B = [int(A[i]) for i in range(len(A))]
    for i in range(N-K+1):
        prod = 1
        for j in range(K):
            prod = prod * B[i+j]
        if i==0:            
            res = prod
        else:
            res = max(res,prod)
    print res
