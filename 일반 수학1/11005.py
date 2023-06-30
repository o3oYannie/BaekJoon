def convert(N,B):
    num="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    a,b = divmod(N,B)
    if a==0 :
        return num[b]
    else:
        return convert(a,B)+num[b]

N,B = input().split()
N=int(N)
B=int(B)
print(convert(N,B))