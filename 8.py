#8: Tính S(n) = ½ + ¾ + 5/6 + … + 2n + 1/ 2n + 2
n=1
tong=0
n=int(input())
for i in range(1, n+1):
    tong += 1/(2*i+2)
print("S(n) = ",tong)