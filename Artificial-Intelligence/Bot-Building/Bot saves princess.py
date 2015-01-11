#!/bin/python
def displayPathtoPrincess(x,y):
    while x!=0:
        if x<0:
            print "DOWN"
            x = x+1
        else:
            print "UP"
            x = x-1
    while y!=0:
        if y<0:
            print "RIGHT"
            y = y+1
        else:
            print "LEFT"
            y = y-1
#print all the moves here
m = input()

grid = []
for i in xrange(0, m):
    T = raw_input()
    x = T.find('p')
    if x != -1:
        rp = i
        cp = x
    x2 = T.find('m')
    if x2 != -1:
        rm = i
        cm = x2
    grid.append(T)

displayPathtoPrincess(rm-rp,cm-cp)
