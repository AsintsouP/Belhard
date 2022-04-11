number1 = float(input('Введите первое число '))
number2 = float(input('Введите второе число '))
number3 = float(input('Введите третье число '))
positive = f'Количество положителььных: {(number1 > 0) + (number2 > 0) + (number3 > 0)}'
negative = f'Количество отрицательных: {(number1 < 0) + (number2 < 0) + (number3 < 0)}'
print(positive)
print(negative)
