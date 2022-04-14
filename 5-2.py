# Сделать калькулятор: у пользователя спрашивается число, потом действие и второе число
number_0 = int(input('Введите сичло '))
action = input('Введите дейтсвие (+, -, *, /) ')
number_1 = int(input('Введите сичло '))
if action == '+':
    print(number_0+number_1)
elif action == '-':
    print(number_0-number_1)
elif action == '*':
    print(number_0 * number_1)
elif action == '/':
    print(number_0 / number_1)
