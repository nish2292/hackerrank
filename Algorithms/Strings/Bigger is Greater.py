def lnp(a):
    i = len(a) - 2
    while not (i < 0 or a[i] < a[i+1]):
        i -= 1
    if i < 0:
        return False
    # else
    j = len(a) - 1
    while not (a[j] > a[i]):
        j -= 1
    a[i], a[j] = a[j], a[i]        # swap
    a[i+1:] = reversed(a[i+1:])    # reverse elements from position i+1 till the end of the sequence
    print "".join(a)

T = input()
while T>=1:
    X = list(raw_input())
    N = len(X)
    s = 0
    while s<(N-1):
        if X[s]>=X[s+1]:
            s+=1
        else:
            break
    
    if s == N-1:
        print "no answer"
        T-=1
        continue
    #res = "".join(X[0:s])
    lnp(X)
    T-=1
