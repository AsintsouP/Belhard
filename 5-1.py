# Внести первые N чисел кратные M и больше K
k = 50
m = 2
n = 3
for i in range(k, 100):
    if i % m == 0 and i > k:
        print(i)
