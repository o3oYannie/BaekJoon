a=['A+','A0','B+','B0','C+','C0','D+','D0','F']
b=[4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]
avg=0
score=0
for i in range(20):
    s,sc,g=input().split()
    if(g!='P'):
        sc=float(sc)
        score=score+sc
        avg+=(b[a.index(g)]*sc)
print('%.6f' %(avg/score))