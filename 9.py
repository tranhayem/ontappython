#9: Tính T(n) = 1 x 2 x 3…x N
n=1
tich=1
n=int(input())
for i in range(1, n+1):
    tich *= i
print("T(n) = ",tich)