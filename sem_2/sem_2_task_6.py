a = input().split()
print(" ".join([i for i in a if a.count(i) == 1]))