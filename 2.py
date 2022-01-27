#2: Tính S(n) = 1^2 + 2^2 + … + n^2
n=1
tong=0
n=int(input())
for i in range(1, n+1):
    tong += i**2
print("S(n) = ",tong)