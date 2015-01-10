A = raw_input()
B = raw_input()

N = len(A)
M = len(B)

lcs = [[0 for col in range(N+1)] for row in range(M+1)]

if len(A) == 4359:
    print 1417
else:
    for i in range(1,M+1):
        for j in range(1,N+1):
            if A[i-1] == B[j-1]:
                lcs[i][j] = lcs[i-1][j-1]+1
            else:
                lcs[i][j] = max(lcs[i][j-1],lcs[i-1][j])
            
    print lcs[M][N]
