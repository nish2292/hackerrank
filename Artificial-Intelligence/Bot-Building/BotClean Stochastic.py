#!/usr/bin/python
def nextMove(MV,MH):
    
    #MV = rd - r
    #MH = cd - c
    if MH==0 and MV==0:
        print 'CLEAN'
        return
    if abs(MH)>abs(MV):
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
    pos = [int(i) for i in raw_input().strip().split()]
    x=-1
    for i in range(5):
        if x==-1:
            x = raw_input().find('d')
            y = i
    rd = y
    cd = x
    MV = rd - pos[0]
    MH = cd - pos[1]
    #board = [[raw_input()] for i in range(5)]
    nextMove(MV,MH)
