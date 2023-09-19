N=int(input())
num = 1
x = 3
#1번 -> 3*3 9 / 2번 -> 5*5 25 /3번 -> 9*9 81/ 4번 -> 17*17 5번 -> 1089
for i in range(1,N):
    num *= 2
    x += num
point = x*x
print(point) # 3+2/ 3+2+4/ 3+2+4+8/ 3+2+4+8+16