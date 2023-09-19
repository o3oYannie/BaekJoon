N=int(input())
a=0
b=1
cnt=0
start=True
while(start):
    cnt+=1
    if N in range(a,b+1):
            start=False
    a=b+1
    b=b+6*cnt
print(cnt)