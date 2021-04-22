n = int(input('Введите сторону квадрата: '))


def square(side_of_the_square):
    return side_of_the_square * 4, side_of_the_square * side_of_the_square, round(side_of_the_square * 2 ** 0.5, 2)


print(square(n))
