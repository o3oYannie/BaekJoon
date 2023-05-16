n,m=map(int,input().split())
b_list=[i for i in range(1,n+1)]
for j in range(0,m):
    a,b=map(int,input().split())
    b_list[a-1], b_list[b-1] = b_list[b-1], b_list[a-1]
print(*b_list)