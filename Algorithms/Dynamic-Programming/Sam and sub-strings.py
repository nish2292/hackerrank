A = raw_input()

count = 1
ans = 0
N = len(A)
weight = 0
for item in A:
    weight = (weight*10 + count*int(item)) % 1000000007
    ans = (ans + weight) % 1000000007
    count = (count +1)
    
print ans
