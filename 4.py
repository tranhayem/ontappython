#4: Tính S(n) = ½ + ¼ + … + 1/2n
n=1
tong=0
n=int(input())
for i in range(1, n+1):
    tong += 1/(2*i)
print("S(n) = ",tong)