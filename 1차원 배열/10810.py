N,M=map(int,input().split())
balls=[0 for i in range(0,N)]
for a in range (0,M):
    i,j,k=map(int,input().split())
    for b in range(i-1,j):
        balls[b]=k
print(*balls)