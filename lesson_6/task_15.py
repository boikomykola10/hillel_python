a = input().split()
B = {}
for key in a:
    B[key] = B.get(key, 0) + 1
print(B)