T = input()
M = 1000000007
for t in range(T):
    N = input()
    A = map(int,raw_input().strip().split())
    sum = 0
    for i in range(N):
        sum = sum | A[i]
    sum = (sum << (N-1)) % M
    print sum
