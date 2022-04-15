# Вывести четные числа от 2 до N по 5 в строку
N = int(input('max number: '))
K = int(input('count: '))
count = 0
for i in range(3, N+1, 3):
    if count < K:
        print(i, end=' ')
        count += 1
    else:
        count = 1
        print(i)

