T=int(input())
sum=[]
for i in range(1,T+1):
    A,B=map(int,input().split())
    sum.append(A+B)
for j in range(0,T):
    print("Case #%d: %d"%(j+1,sum[j]))