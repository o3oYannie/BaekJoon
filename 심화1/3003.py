a=list(map(int,input().split()))
b=[1,1,2,2,2,8]
c=[]
for i in range(0,6):
    c.append(b[i]-a[i])
for i in c:
    print(i,end=' ')