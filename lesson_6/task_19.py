import random

print(len(set([random.randint(5, 15) for _ in range(10)]) ^ set([random.randint(10, 20) for _ in range(10)])))
