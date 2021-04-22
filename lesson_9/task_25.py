n = int(input('Введите номер месяца от 1 до 12: '))


def season(number):
    if 3 <= number <= 5:
        return 'Spring'
    elif 6 <= number <= 8:
        return 'Summer'
    elif 9 <= number <= 11:
        return 'Autumn'
    else:
        return 'Winter'


print(season(n))
