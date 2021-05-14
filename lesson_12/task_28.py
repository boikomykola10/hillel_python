from pprint import pprint

file1 = open('src_14.txt', encoding='utf-8')
lst = []
file2 = open('task_28.txt', 'w')
for line in file1:
    lst.append(line.strip('\n').split())

average = 0
for line in lst:
    sum_line = 0
    for j in line[2:]:
        sum_line += round(int(j) / len(line[2:]), 2)
    average += sum_line / round(len(lst))
    file2.write(line[1] + ' ' + line[0][0] + '.' + str(sum_line))
    file2.write('\n')
    if sum_line < 5:
        print(line[0], line[1], sum_line)
print('Средний бал класса:', round(average, 2))










