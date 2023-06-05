n=int(input())
c=n
for i in range(n):
    string=input()
    for j in range(0,len(string)-1):
        if string[j]==string[j+1]:
            pass
        elif string[j] in string [j+1:]:
            c=c-1
            break
print(c)