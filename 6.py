#6: Tính S(n) = 1/1×2 + 1/2×3 +…+ 1/n x (n + 1)
n=1
tong=0
n=int(input())
for i in range(1, n+1):
    tong += 1/(i*(i+1))
print("S(n) = ",tong)