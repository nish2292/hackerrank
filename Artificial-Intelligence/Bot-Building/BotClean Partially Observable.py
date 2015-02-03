def nextMove(MV,MH,f,r,c):
    
    #MV = rd - r
    #MH = cd - c
    if MH==0 and MV==0 and f==1:
        print 'CLEAN'
        return
    elif MH==0 and MV==0 and f==0:
        if r in range(0,3) and c in range(0,2):
            print 'DOWN'
        elif r in range(3,5) and c in range(0,3):
            print 'RIGHT'
        elif r in range(2,5) and c in range(3,5):
            print 'UP'
        elif r in range(0,2) and c in range(2,5):
            print 'LEFT'
        else:
            print 'DOWN'
        return
    if abs(MH)>=abs(MV):
        if MH<0:
            print 'LEFT'
        else:
            print 'RIGHT'
    else:
        if MV>=0:
            print 'DOWN'
        else:
            print 'UP'
            
if __name__ == "__main__":
     
    r,c = map(int,raw_input().strip().split())
    
    #R,C = map(int,raw_input().strip().split())
    
    dmax = 25
    rm = r
    cm = c
    f = 0
    for i in range(5):
        r1 = i
        T = raw_input()
        for j in range(5):
            if T[j] == 'd':
                c1 = j 
                dist = pow((r-r1),2) + pow((c-c1),2)
                if dist<=dmax:
                    f = 1
                    rm = r1
                    cm = c1
                    dmax = dist
    MV = rm - r
    MH = cm - c       
    nextMove(MV,MH,f,r,c)
