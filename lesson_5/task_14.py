import random

lst = [random.randrange(1, 20, 1) for _ in range(15)]
print(lst)
k = int(input('Введите индекс элемента: '))
for i in range(k, len(lst)-1):
    lst[i] = lst[i+1]
lst.pop()
print(lst)


