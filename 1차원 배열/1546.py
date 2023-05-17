n=int(input())
sum=0
score=list(map(int,input().split()))
for i in range(0,n):
    sum=sum+(score[i]/max(score))*100
print(float(sum/n))