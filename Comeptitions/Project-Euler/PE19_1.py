import time
from math import floor
M = [[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31], [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]]

def day_of_week(year, month, day):
    d = day
    m = (month - 3) % 12 + 1
    if m > 10: Y = year - 1
    else: Y = year
    y = Y % 100
    c = (Y - (Y % 100)) / 100 
    w = (d + floor(2.6 * m - 0.2) + y + floor(y/4) + floor(c/4) - 2*c) % 7 
    return int(w)

def Mind(y):
    return min(y%400,max(min(y%4,1),1-y%100))

def nearest_first(y,m,d):
    if d!=1:
        if m == 12:
            m = 1
            y = y+1
        else:
            m = m+1
    while day_of_week(y,m,1) != 0:
        y += int(m/12)
        m %= 12
        m += 1
    return (y,m,1)

def bef(Y1,M1,D1,Y2,M2,D2):
    if Y1>Y2:
        return False
    elif Y1==Y2 and M1>M2:
        return False
    elif Y1==Y2 and M1==M2 and D1>D2:
        return False
    else:
        return True

def cnt(Y1,M1,D1,Y2,M2,D2):
    c = 0
    while bef(Y1,M1,D1,Y2,M2,D2):
        c += 1
        sm = M[Mind(Y1)][M1-1]
        Y1 = Y1 + int(M1/12)
        M1 = (M1%12) + 1
        while sm%7 != 0:
            sm += M[Mind(Y1)][M1-1]
            Y1 = Y1 + int(M1/12)
            M1 = (M1%12) + 1  
    return c

T = input()

for t in range(T):
    Y1,M1,D1 = map(int,raw_input().strip().split())
    Y2,M2,D2 = map(int,raw_input().strip().split())
    Y1,M1,D1 = nearest_first(Y1,M1,D1)
    print cnt(Y1,M1,D1,Y2,M2,D2)

