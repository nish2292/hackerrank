N = input()
A = []
for i in range(N):
    T = input()
    A.append(T)
    
UP = [1] * N
DN = [1] * N

for i in range(1,N):
    if(A[i-1]<A[i]):
        UP[i] = UP[i-1]+1
    if(A[N-i]<A[N-1-i]):
        DN[N-i-1] = DN[N-i] + 1

cnt = 0
R = [max(UP[i],DN[i]) for i in range(N)]
print sum(R)
        
