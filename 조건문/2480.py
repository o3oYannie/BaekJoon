#같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다. 
#같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다. 
#모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.  
a,b,c=map(int,input().split())
money=0
if(a==b and b==c):
    money=10000+a*1000
elif(a==b or a==c or b==c):
    if((a==b and a!=c) or (a==c and a!=b)):
        money=1000+a*100
    elif(b==c and a!=b):
        money=1000+b*100
elif(a!=b and a!=c and b!=c):
    if(a>b and a>c):
        money=a*100
    elif(b>a and b>c):
        money=b*100
    else:
        money=c*100
print(money)
        