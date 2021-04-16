a = input().lower().split()
B = {}
for key in a:
    B[key] = B.get(key, 0) + 1
max_count = max(B.values())
k = ''
for key, value in B.items():
    if value == max_count:
        k, key = key, k
print(k)
