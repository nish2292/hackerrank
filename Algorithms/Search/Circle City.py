import math

def is_sqr(n):
    if n == pow(int(math.sqrt(n)),2):
        return 1
    else:
        return 0

T = input()
 
for t in range(T):
    
    r,k = map(int,raw_input().strip().split())
    #if k==0:
    #    print 'impossible'
    #    continue
    c = 0
    X = range(0,int(math.ceil(math.sqrt(r))))
    for x in X:
        if is_sqr(r-x*x):
            c = c+4
    if c<=k:
        print 'possible'
    else:
        print 'impossible'
