import math
def prime_sieve(limit):
    limitn = limit+1
    not_prime = [False] * limitn
    primes = []

    for i in range(2, limitn):
        if not_prime[i]:
            continue
        for f in xrange(i*2, limitn, i):
            not_prime[f] = True

        primes.append(i)

    return primes

T = input()
for t in range(T):
    N = input()
    prod = 1
    T1 = prime_sieve(N)
    #print T1
    for i in T1:
        x = int(math.log(N,i))
        x = pow(i,x)
        prod = prod*x
    print prod
