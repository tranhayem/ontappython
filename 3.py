#3: Tính S(n) = 1 + ½ + 1/3 + … + 1/n
n=1
tong=0
n=int(input())
for i in range(1, n+1):
    tong += 1/i
print("S(n) = ",tong)