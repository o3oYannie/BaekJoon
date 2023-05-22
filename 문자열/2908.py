a,b=map(int,input().split())
li=[]
a2=int(str(a)[::-1])
b2=int(str(b)[::-1])
li.append(a2)
li.append(b2)
print(max(li))