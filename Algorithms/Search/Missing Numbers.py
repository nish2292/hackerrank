# Enter your code here. Read input from STDIN. Print output to STDOUT
N = input()
A = map(int,raw_input().strip().split())
A.sort()
M = input()
B = map(int,raw_input().strip().split())
B.sort()

else:
    i=0
    j=0
    C = []
    while j<M:
        if(A[i]==B[j]):
            i=i+1
            j=j+1
        elif (A[i]>B[j]):
            C.append(B[j])
            j=j+1
    
    print C[0],
    i=1
    while i<len(C):
        if (C[i]!=C[i-1]):
            print C[i],
        i = i+1
