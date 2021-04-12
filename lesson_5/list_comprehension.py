import random
"""
                1      /        2
new_list = [ expression for item in list ]

                1      /        2        /      3
new_list = [ expression for item in list if conditional ]
"""

""" lst0 = []
for _ in range(15):
    lst0.append(round(random.uniform(1, 100), 2))
print(lst0)

lst1 = [round(random.uniform(1, 100), 2) for _ in range(15)]
print(lst1)

lst2 = [int(element) for element in lst1 if element > 20]
print(lst2)
"""

lst = [random.randint(1, 10) for _ in range(15)]
print(lst)

lst = [x for x in lst if x % 2 == 0]
print(lst)

lst = [x for x in range(1, 25, 2)]
print(lst)

lst = [x**2 for x in range(1, 25, 2)]
print(lst)

lst = [x**2 for x in range(1, 25, 2) if x % 3 != 0]
print(lst)
