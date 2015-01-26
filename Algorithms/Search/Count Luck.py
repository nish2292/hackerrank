T = input()
Kval = 0 
def find(A,N):
    for i in range(N):
        j = A[i].find('M')
        if j != -1:
            return i,j

def dfs(A,x,y,N,M):
    if A[x+1][y+1]=='*':
        return 1

    A[x+1][y+1] = 'X'
    t1,t2,t3,t4 = 0,0,0,0
    c = 0
    if A[x+2][y+1] != 'X':
        c+=1
        t1 = dfs(A,x+1,y,N,M)
    if A[x+1][y+2] != 'X':
        c+=1
        t2 = dfs(A,x,y+1,N,M)
    if A[x][y+1] != 'X':
        c+=1
        t3 = dfs(A,x-1,y,N,M)
    if A[x+1][y] != 'X':
        c+=1
        t4 = dfs(A,x,y-1,N,M)
    ret = max(t1,t2,t3,t4)
    if c>1 and ret!=0:
        global Kval
        Kval += 1
    return ret
    
    

for t in range(T):
    N,M = map(int,raw_input().strip().split())
    A = []
    Xs = ['X' for i in range(M+2)]
    A.append(Xs)
    global Kval
    Kval = 0
    for i in range(N):
        T = raw_input()
        j = T.find('M')
        T = 'X' + T + 'X'
        A.append(list(T))
        if j != -1:
            posx, posy = i,j
    A.append(Xs)  
    res = dfs(A,posx,posy,N,M)
    K = input()
    if K==Kval:
        print 'Impressed'
    else:
        print 'Oops!'
