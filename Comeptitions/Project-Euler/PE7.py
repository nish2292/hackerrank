def primes_sieve(limit):
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
# Enter your code here. Read input from STDIN. Print output to STDOUT

T = input()
P = primes_sieve(150000) 
#print len(P), P[0]
for t in range(T):
    N = input()
    print P[N-1]
