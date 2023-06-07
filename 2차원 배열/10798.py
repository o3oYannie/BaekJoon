s = [input() for i in range(5)]
new=[]
for j in range(15):
    for i in range(5):
        if(j<len(s[i])):
            new.append(s[i][j])
for i in range(len(new)):
    print(new[i],end='')