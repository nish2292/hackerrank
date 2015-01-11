T = input()

def sum1(m,n):
    if m==1 and n==1:
        return 2
    elif n==1 or m==1:
        return 1
    elif n==2 and m==2:
        return 1
    else:
        return 0

for t in range(T):
    N = input()
    A = map(int, raw_input().strip().split(" "))
    #sum = 0
    ones = 0
    twos = 0
    for i in range(N):
        if A[i] == 1:
            ones = ones+1
        elif A[i] == 2:
            twos = twos+1
    oth = N-ones
    sum = oth * ones
    sum = sum + ones*(ones-1)
    sum = sum + twos*(twos-1)/2
    #for i in range(N):
    #    for j in range(i+1,N):
    #        sum = sum + sum1(A[i],A[j])
    print sum
