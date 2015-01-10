import math

T = input()

for t in range(T):
    A = map(int, raw_input().strip().split(" "))
    N = A[0]
    m = A[1]
    mul = int(N/m)
    #print sum,m
    #sum = sum * m
    #print sum
    rd = N % m
    sum1=0
    sum1 = (m-1)*(m)/2
    sum1 = sum1*mul
    sum1 = sum1 + (rd)*(rd+1)/2
    #for i in range(1,rd+1):
    #    sum1 = sum1 + (i%m)
    print sum1
