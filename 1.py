#1: Tính S(n) = 1 + 2 + 3 + … + n
n=1
tong=0
n=int(input())
for i in range(1, n+1):
    tong += i
print("S(n) = ",tong)