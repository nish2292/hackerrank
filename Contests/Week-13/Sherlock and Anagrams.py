from collections import Counter

P = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,91,101]
#print len(P)

T =input()
#T=1

for t in range(T):
    S = raw_input()
    #S = 'abcba'
    arr = [P[ord(x)-97] for x in S]
    N = len(arr)
    count = 0
    j=0
    for i in range(1,N-1):
        #print i
        for st in range(0,N-i):
            temp = arr[j+st] * arr[i+st]       
            arr.append(temp)
        j = j + (N+1-i)
        #print j
    arr.sort()
    #print arr
    cntr = Counter(arr).items()
    for x,y in cntr:
        #print x,y
        if(y>1):
            count = count + (y*(y-1)/2)
    print count
