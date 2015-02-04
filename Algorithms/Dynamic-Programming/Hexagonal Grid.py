T = input()

for t in range(T):
    
    N = input()
    A = raw_input()
    tA = A.count('1')
    B = raw_input()
    tB = B.count('1')
    
    if (tA+tB) % 2 == 1:
        print 'NO'
        continue
    
    i = 0
    j = 0
    f = 1
    while(i<N and j<N):
        #print i,j
        if A[i] == B[j]:
            i += 1
            j += 1
            continue
        
        if (j+1>=N):
            
            if (i+1>=N):
                print 'NO'
                f = 0
                i += 1
                break
            elif(A[i+1] == '0'):
                C = A
                A = B
                B = C
                t = i
                i = j
                j = t
                i += 1
                j += 2
        elif (A[i+1] == '1' and B[j+1] == '1'):
            print 'NO'
            f = 0
            i += 1
            break
        elif (A[i+1] == '1' and B[j+1] == '0' and B[j]=='1'):
            print 'NO'
            f = 0
            i += 1
            break
        elif (A[i+1] == '1' and B[j+1] == '0' and A[i]=='1'):
            i+=2
            j+=2
        elif (A[i+1] == '0' and B[j+1] == '1' and B[j]=='1'):
            i+=2
            j+=2
        elif A[i+1] == '0':
            C = A
            A = B
            B = C
            t = i
            i = j
            j = t
            i += 1
            j += 2
            
    if f==1:
        print 'YES'
