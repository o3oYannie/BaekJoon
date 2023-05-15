a=int(input())
num_List=[]
for i in range(0,a):
    num1,num2=map(int,input().split())
    num_List.append(num1+num2)
for j in range(0,a):
    print("%d"%(num_List[j]))
    