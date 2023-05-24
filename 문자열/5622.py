string = input()
time=0
dial=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
for i in range(len(string)):
    for j in dial:
        if string[i] in j:
            time+=dial.index(j)+3
print(time)
        