i = int(input())
a = [int(j) for j in input().split()]
print(sorted(a)[i//2])