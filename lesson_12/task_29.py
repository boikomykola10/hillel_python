file = open('task_29.txt', 'tw')
while True:
    s = input()
    if s == '':
        break
    file.write(s)
    file.write('\n')
file.close()
