H,M=map(int, input().split()) #23 20 +25 >>> 0 13
O=int(input())
M=M+O 
if(M>=60):
    H=H+(M//60)  
    M=M%60 
if(H>=24):
    H=H-24 
print(H, M)