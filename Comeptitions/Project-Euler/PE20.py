from math import factorial
T = input()

for t in range(T):
    N = input()
    F = factorial(N)
    S  =str(F)
    P = [(ord(x)-48) for x in S]
    res= sum(P)
    print res
