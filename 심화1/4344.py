case = int(input())
for i in range(0,case):
    n=list(map(int,input().split()))
    avg= sum(n[1:])/n[0]
    h=0
    for j in range(1,len(n)):
        if n[j]>avg:
            h=h+1
    cnt=(h/n[0]*100)
    print(f'{cnt:.3f}%')
        