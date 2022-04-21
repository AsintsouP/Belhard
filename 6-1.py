# Написать функцию перевода десятичного числа в двоичное и обратно
def decimal_to_binary(decimal):
    binary = []

    while decimal > 0:
        binary.append(decimal % 2)
        decimal // 2

    binary.reverse()

    return binary

