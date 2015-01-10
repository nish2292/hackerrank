def pow2sum(exp):
    pow = list(str(2**exp))
    return sum([int(i) for i in pow])

T = input()

for i in range(T):
    N = input()
    print pow2sum(N)
