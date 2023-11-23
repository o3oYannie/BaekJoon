X=int(input())
cnt=1
n=2
up = 1
down = 1
while(X>1):
    X=X-cnt 
    if (X>cnt) :
        cnt = cnt + 1
    else :
        if(X==0): 
            X = X + cnt
            cnt = cnt - 1
        n = cnt + 2
        break
if(cnt%2==0):
    up = n - X
    down = X
else:
    up = X
    down = n - X
print(str(up)+'/'+str(down))