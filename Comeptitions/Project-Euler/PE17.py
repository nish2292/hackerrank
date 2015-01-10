Te = input()
ones = ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
ten = ['Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
tens = ['Ten','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
ten3 = ['Hundred','Thousand','Million','Billion']

for t in range(Te):
    
    N = input()
    if N==0:
        print 'Zero'
        continue
    elif N==1000000000000:
        print 'One Trillion'
        continue
    p=0
    opt = []
    while N!=0:
        res = ''
        T = N%1000
        if T==0:
            N = int(N/1000)
            p = p + 1
            continue
        T1 = int(T/100)
        if T1>0:
            res = res + ones[T1] + ' ' + ten3[0]
            #print ones[T1],ten3[0],
        
        if T%100 < 20 and T%100 >=10:
            X = (T%100) - 10
            if len(res) == 0:
                res = res + ten[X]
            else:
                res = res + ' ' + ten[X]
            #print ten[X],
        else:
            
            X = int(T/10)
            X = X%10
            if X>0:
                
                if len(res) == 0:
                    res = res + tens[X-1]
                else:
                    res = res + ' ' + tens[X-1]
                #print tens[X-1],
            X = T%10
            if X>0:
                if len(res) == 0:
                    res = res + ones[X]
                else:
                    res = res + ' ' + ones[X]
            #res = res + ' ' + ones[X]
                #print ones[X],
        N = int(N/1000)
        p = p + 1
        if(p>1) and len(res)!=0:
            res = res + ' ' + ten3[p-1]
            #print ten3[p-1],
        if len(res)!=0:
            opt.append(res)
    #print
    for i in range(len(opt)):
        X = len(opt) - 1 -i
        print opt[X],
    print
