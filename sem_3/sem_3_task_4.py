a = input().split()
n = int(a[0])

for i in range(n+1):
    z = n//2 + 1 - abs(i - n//2)
    print(a[1]*z)