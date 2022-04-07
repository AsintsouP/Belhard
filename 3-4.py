number1 = float(input('Введите первое число '))
number2 = float(input('Введите второе число '))
number3 = float(input('Введите третье число '))
positive = 0
negative = 0
if number1 > 0:
    positive += 1
if number2 > 0:
    positive += 1
if number3 > 0:
    positive += 1
if number1 < 0:
    negative += 1
if number2 < 0:
    negative += 1
if number3 < 0:
    negative += 1
print(f'Положительных {positive}')
print(f'Отрицательных {negative}')