
file1 = open('src_14.txt', encoding='utf-8')
lst = []
file2 = open('task_28.txt', 'w')
for line in file1:
    lst.append(line.strip('\n').split())

average_student = 0
average_class = 0
for line in lst:
    sum_line = 0
    for j in line[2:]:
        sum_line += int(j)
    average_student = round(sum_line / len(line[2:]), 2)
    average_class += average_student
    file2.write('{:20}'.format(str(line[1]+' ') + str(line[0][0] + '.')) + str(average_student))
    file2.write('\n')
    if average_student < 5:
        print('{:21}'.format(str(line[0])+' ' + str(line[1]) + ' ') + str(average_student))
print('Средний бал класса: ', round(average_class / len(lst), 2))
