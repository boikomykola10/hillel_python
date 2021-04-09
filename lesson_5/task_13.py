import random

lst = [random.randint(150, 200) for _ in range(20)]
lst.sort(reverse=True)
print(lst)
X = int(input('Введите рост Пети: '))
for i in range(len(lst)):
    if X > lst[i]:
        print(i)
        break
else:
    print(len(lst))
