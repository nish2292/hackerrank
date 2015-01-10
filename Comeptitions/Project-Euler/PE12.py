def facts(lim,inp):
    F = [2] * (lim+1)
    F[0] = 0
    F[1] = 1
    F[2] = 1
    for i in range(3,lim+1):
        if i%2 == 0:
            T = i/2
            if T%2 == 1:
                F[i] = F[T]
                continue
        else:
            T = i
        for j in range(2, T):
            if T%j == 0:
                F[i] = F[i] + 1
    #print N
    #for i in range(len(F)):
    #    print i,F[i]

    op = [0] * len(inp)
    for ip in range(len(inp)):
        T = inp[ip]
        for i in range(2,len(F)):
            prod = F[i]*F[i-1]
            if prod>T:
                op[ip] = i*(i-1)/2
                break
        
                
    for x in op:
        print x
    #mx = 1
    #for i in range(2,len(F)):
        #prod = F[i]*F[i-1]
        #mx = max(mx,prod)
    #print
    #print mx

T = input()


inp = [0] * T

inp = [input() for i in range(T)]
lim = max(inp)
facts(30*lim,inp)
