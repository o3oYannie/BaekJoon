s=input()
lst=list(s)
alphabet='abcdefghijklmnopqrstuvwxyz'
m=0
for i in alphabet:
    n=lst.count(i)+lst.count(i.upper())
    if(m<n):
        m=n
        alp=i.upper()
    elif(m==n):
        alp='?'
print(alp)