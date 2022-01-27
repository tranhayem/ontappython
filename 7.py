#7: Tính S(n) = ½ + 2/3 + ¾ + …. + n / n + 1
n=1
tong=0
n=int(input())
for i in range(1, n+1):
    tong += i/(i+1)
print("S(n) = ",tong)