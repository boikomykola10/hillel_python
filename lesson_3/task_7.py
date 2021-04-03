number = int(input('Введите целое число: '))
summa = 0
amount = 0
odd_number = 0
even_number = 0
average = 0
max_number = number
min_number = number
while number != 0:
    summa += number
    amount += 1
    average = summa / amount
    if number % 2 == 0:
        odd_number += 1
    else:
        even_number += 1
    if number > max_number:
        number, max_number = max_number, number
    elif number < min_number:
        number, min_number = min_number, number
    number = int(input('Введите целое число: '))
print(summa, amount, average, odd_number, even_number, max_number, min_number)
