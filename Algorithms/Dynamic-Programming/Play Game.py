T= input()
#def mx(A,l,h,Dp):
#    if l>h:
#        return 0
#    if Dp[l] != -1:
#        return Dp[l]
#    
#    c1,c2,c3 = 0,0,0
#    c1 = A[l] + min(mx(A,l+2,h,Dp),mx(A,l+3,h,Dp),mx(A,l+4,h,Dp))
#    if l<h:
#        c2 = A[l] + A[l+1] + min(mx(A,l+3,h,Dp),mx(A,l+4,h,Dp),mx(A,l+5,h,Dp))
#    if (l+1)<h:
#        c3 = A[l] + A[l+1] + A[l+2] + min(mx(A,l+4,h,Dp),mx(A,l+5,h,Dp),mx(A,l+6,h,Dp))
#    Dp[l] = max(c1,c2,c3)
#    return Dp[l]

for t in  range(T):
    N = input()
    A = map(int,raw_input().strip().split())
    
    #Dp = [-1] * (N+10)
    #res = mx(A,0,N-1,Dp)
    #print Dp
    if N<4:
        print sum(A)
        continue
    Dp = [0] * (N+10)
    Dp[N-1] = A[N-1]
    Dp[N-2] = A[N-2] + Dp[N-1]
    Dp[N-3] = A[N-3] + Dp[N-2] 
    
    i = N-4
    while i>=0:
        c1,c2,c3 = 0,0,0
        c1 = A[i] + min(Dp[i+2],Dp[i+3],Dp[i+4])
        if i < N-1:
            c2 = A[i] + A[i+1] + min(Dp[i+3],Dp[i+4],Dp[i+5])
        if (i+1)< N-1:
            c3 = A[i] + A[i+1] + A[i+2] + min(Dp[i+4],Dp[i+5],Dp[i+6])
        Dp[i] = max(c1,c2,c3)
        i -= 1
    print Dp[0]
