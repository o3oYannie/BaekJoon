import sys
T=int(sys.stdin.readline())
T_List=[]
for i in range(0,T):
    a,b=map(int,sys.stdin.readline().split())
    T_List.append(a+b)
for j in range(0,T):
    print(T_List[j])