import random

lst = [random.randint(1,20) for _ in range(15)]
print(lst)
count = 0
for i in range(1, len(lst)-1):
    if lst[i - 1] < lst[i] < lst[i + 1]:
        count += 1
print(count)
