# Внести первые N чисел кратные M и больше K
N = int(input('количество'))
M = int(input('кратные'))
K = int(input('нижний предел'))
count = 0
while count < N:
    if not K % M:
        print(K)
        count += 1
    K += 1
