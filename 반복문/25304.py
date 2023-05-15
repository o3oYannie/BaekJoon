price=int(input()) #영수증 가격
num=int(input()) #구매물건 종류 개수
sum=0
for i in range(0,num):
    a,b=map(int,input().split())
    sum=sum+a*b
if(price==sum):
    print("Yes")
else:
    print("No")