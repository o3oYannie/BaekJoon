#쿼터(Quarter, $0.25)의 개수, 다임(Dime, $0.10)의 개수,
#니켈(Nickel, $0.05)의 개수, 페니(Penny, $0.01)
N=int(input())
for i in range(0,N):
    a=int(input())
    for j in [25,10,5,1]:
        print(a//j,end=' ')
        a=a%j