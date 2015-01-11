#!/bin/python
def nextMove(n,r,c,grid,rp,cp):
    RD = r - rp
    CD = c - cp
    #print RD,CD
    if abs(RD) <= abs(CD):
        if CD>0:
           return "LEFT"
        else:
           return "RIGHT"
    else:
        if RD<0:
           return "DOWN"
        else:
           return "UP"

    
n = input()
r,c = [int(i) for i in raw_input().strip().split()]
grid = []
for i in xrange(0, n):
    T = raw_input()
    x = T.find('p')
    if x != -1:
        rp = i
        cp = x
    grid.append(T)
    

print nextMove(n,r,c,grid,rp,cp)
