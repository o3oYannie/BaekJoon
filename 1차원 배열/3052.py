List=[0 for i in range(10)]
List2=[]
for i in range(0,10):
    List[i]=int(input())
for j in range(0,10):
    a=List[j]%42
    if a not in List2:
        List2.append(a)
print(len(List2))
    