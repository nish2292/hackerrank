def LPS(A):
    Arev = A[::-1]
    N = len(A)
    L = [[0 for i in range(N+1)] for j in range(N+1)]
    for i in range(1,N+1):
        L[1][i] = 1

    for i in range(2,N):
        for j in range(0,N-i+1):
            if A[j] == A[j+i-1]:
                L[i][j+1] = 2 + L[i-2][j+2]
            else:
                L[i][j+1] = max(L[i-1][j+1],L[i-1][j+2])

    res = 0
    for i in range(1,N-1):
        res = max(L[i][1] * L[N-i][i+1],res)
    return res

print LPS(raw_input())
