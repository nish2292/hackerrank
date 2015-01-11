T=input()

for t in range(T):
    
    N = input()
    A = map(int, raw_input().strip().split())
    
    pft = 0
    nsh = 0
    loss = 0
    
    mn = 0
    for i in range(N)[::-1]:
        mn = max(mn,A[i])
        pft = pft + mn - A[i]
    
    print pft
