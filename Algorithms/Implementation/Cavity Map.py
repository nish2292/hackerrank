T = input()
grid = []

for t in range(T):
    I = list(raw_input())
    grid.append(I)
    
print ''.join(grid[0])
for i in range(1,T-1):
    st = [grid[i][j] for j in range(T)]
    for j in range(1,T-1):
        if (ord(grid[i][j])>ord(grid[i][j-1])) and (ord(grid[i][j])>ord(grid[i][j+1])) and (ord(grid[i][j])>ord(grid[i-1][j])) and (ord(grid[i][j])>ord(grid[i+1][j])):
            st[j] = 'X'
    print ''.join(st)
if T>1:
    print ''.join(grid[T-1])
