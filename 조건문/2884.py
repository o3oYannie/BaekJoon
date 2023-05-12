H, M =map(int, input().split()) #11.40>10.55
if(M<45):
    M=M+(60-45)
    if(H<1):
        H=24-1
    else:
        H=H-1
else:
    M=M-45
print(H, M)