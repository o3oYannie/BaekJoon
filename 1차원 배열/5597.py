List=[0 for i in range(28)]
for i in range(0,28):
    n=int(input())
    List[i]=n
for i in range(1,31):
    if i not in List:
        print(i)