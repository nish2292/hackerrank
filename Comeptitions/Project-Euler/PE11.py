A = []
for i in range(20):
    T = map(int,raw_input().strip().split())
    A.append(T)
    
res = 0

for i in range(20):
    for j in range(17):
        prod = A[i][j] * A[i][j+1] * A[i][j+2] * A[i][j+3]
        res = max(prod,res)

for i in range(17):
    for j in range(20):
        prod = A[i][j] * A[i+1][j] * A[i+2][j] * A[i+3][j]
        res = max(prod,res)        
        
for i in range(17):
    for j in range(17):
        prod = A[i][j] * A[i+1][j+1] * A[i+2][j+2] * A[i+3][j+3]
        res = max(prod,res)
        
for i in range(17):
    for j in range(3,20):
        prod = A[i][j] * A[i+1][j-1] * A[i+2][j-2] * A[i+3][j-3]
        res = max(prod,res)
        
print res
