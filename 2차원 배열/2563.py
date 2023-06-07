arr = [[0]*100 for _ in range(100)]
cnt=0
n=int(input())
for i in range(0,n):
    x,y=map(int,input().split())
    for a in range(x,x+10):
        for b in range(y,y+10):
            arr[a][b]=1
for i in arr:
    cnt+=i.count(1)
print(cnt)