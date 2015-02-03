#!/usr/bin/python
def nextMove(MV,MH):
    
    #MV = rd - r
    #MH = cd - c
    if MH==0 and MV==0:
        print 'CLEAN'
        return
    if abs(MH)>=abs(MV):
        if MH<0:
            print 'LEFT'
        else:
            print 'RIGHT'
    else:
        if MV>0:
            print 'DOWN'
        else:
            print 'UP'
            
if __name__ == "__main__":
     
    r,c = map(int,raw_input().strip().split())
    
    R,C = map(int,raw_input().strip().split())
    
    dmax = R*C
    rm = -1
    cm = -1
    for i in range(R):
        r1 = i
        T = raw_input()
        for j in range(C):
            if T[j] == 'd':
                c1 = j 
                dist = pow((r-r1),2) + pow((c-c1),2)
                if dist<=dmax:
                    rm = r1
                    cm = c1
                    dmax = dist
    MV = rm - r
    MH = cm - c       
    nextMove(MV,MH)
