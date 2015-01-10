T = input()

while T!=0:
    N = input()
    N1 = N
    c=0
    cnt = 2
    while cnt*cnt <= N1:
        if N1%cnt == 0:
            N1 = N1/ cnt
            c = cnt
            #print N1,cnt
        else:
            cnt = cnt + 1
            #print cnt
    if N1 > c:
        c = N1
        #print c
    print c
    T=T-1
