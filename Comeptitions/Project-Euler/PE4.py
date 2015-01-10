def palindrome(num):
    return str(num) == str(num)[::-1]

A = range(100,1000)
N = len(A)
B = [A[i]*A[j] for i in range(N) for j in range(i,N)]
C = []
for x in B:
    if palindrome(x):
        C.append(x)
C.sort()
res = C
T=input()
while T!=0:
    N = input()
    for i in range(len(res)):
        if res[i] > N:
            print res[i-1]
            break
    T=T-1
