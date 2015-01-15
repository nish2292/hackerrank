T = input()

for t in range(T):
    A,B = map(int,raw_input().strip().split())
    if A==B:
        print A
    else:
        a1 = A%2
        b1 = B%2
        res = 0
        i = 0
        while A>0 or B>0:
            if a1 == b1 and a1==1:
                res = res + 2**i
            elif a1!=b1:
                res = 0
            #print res,A,B
            A = A >> 1
            B = B >> 1
            a1 = A%2
            b1 = B%2
            i = i+1
        print res
