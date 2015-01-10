from datetime import date

def no_sunday(y1,m1,d1):
    count = 0
    y = 1900
    while y<=y1:
        if y==y1:
            k=m1
        else:
            k=12
        for m in range(1,k+1):
            d = date(y, m, 1)
            if d.weekday()==6:
                count = count + 1
        y = y+1
    return count
                
T = input()

for t in range(T):
    Y1,M1,D1 = map(int,raw_input().strip().split())
    Y2,M2,D2 = map(int,raw_input().strip().split())
    res1 = no_sunday(Y1,M1,D1)
    res2 = no_sunday(Y2,M2,D2)
    res = res2-res1
    d = date(Y1,M1,D1)
    if d.weekday()==6:
        res = res + 1
    print res
    
    
