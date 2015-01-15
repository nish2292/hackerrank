N,K = map(int,raw_input().strip().split())
A = raw_input()
A = [ord(x) - ord('0') for x in A]
res = []
N1 = len(A)
res.append(A[N1-1])
for i in range(1,N):
    j = N1-1-i
    temp = A[j]
    t = min(K-1,i)
    ind = len(res) - 1
    #print j,temp,t,ind
    if i>(K-1):
        temp = temp ^ A[j+1] ^ res[ind-K+1]
    elif i ==1:
        temp = temp ^ res[ind]
    else:    
        temp = temp ^ A[j+1]
        #while t!=0:
        #    temp = temp ^ res[ind]
        #    ind = ind-1
        #    t = t-1
    res.append(temp)
B = [str(x) for x in res[::-1]]
print ''.join(B)  
