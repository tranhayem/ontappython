#5: Tính S(n) = 1 + 1/3 + 1/5 + … + 1/(2n + 1)
n=1
tong=0
n=int(input())
for i in range(1, n+1):
    tong += 1/(2*i+1)
print("S(n) = ",tong)