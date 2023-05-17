n,m=map(int,input().split())
bas=[i for i in range(1,n+1)]
for k in range (0,m):
    i,j= map(int,input().split())
    temp=bas[i-1:j]
    temp.reverse()
    bas[i-1:j]=temp
for i in range(n):
    print(bas[i], end = ' ')