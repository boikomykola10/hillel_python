
d = {
    'apple': ['malum', 'pomum', 'popula'],
    'fruit': ['baca', 'bacca', 'popum'],
    'punishment': ['malum', 'multa']
}
c = {}
for key, value in d.items():
    for i in value:
        c[i] = c.get(i, [])
        c[i].append(key)
print(c)
