li=[list(map(int,input().split())) for _ in range(9)]
m=0
mi,mj=0,0
for i in range(9):
    for j in range(9):
        if li[i][j]>=m:
            m=li[i][j]
            mi=i+1
            mj=j+1
print(m)
print(mi,mj)
            