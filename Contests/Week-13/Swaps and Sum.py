N,Q = map(int,raw_input().strip().split())
A =  map(int,raw_input().strip().split())
S = [0]
sum1 = 0 
for x in A:
    sum1 = sum1+x
    S.append(sum1)

for q in range(Q):
    tp,l,r =  map(int,raw_input().strip().split())
    if tp == 2:
        res = S[r] - S[l-1]
        print res
    elif tp ==1:
        i = l-1
        while i < r:
            S[i+1] = S[i+1] - A[i] + A[i+1]
            t = A[i]
            A[i] = A[i+1]
            A[i+1] = t
            i = i+2
