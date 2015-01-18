T = input()
inp = []
for i in range(T):
    inp.append(input())
N = max(inp)
C = [[0 for j in range(N+1)] for i in range(N+1)]
C[0][0] = 1
C[1][0] = 1
C[1][1] = 1
for i in range(2,(N+1)):
    C[i][i] = 1
    C[i][0] = 1
    for j in range(1,i):
        C[i][j] = (C[i-1][j-1] + C[i-1][j]) % 1000000000
#print C
for x in inp:
    for j in range(x+1):
        print C[x][j],
    print
