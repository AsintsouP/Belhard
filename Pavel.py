# Внести первые N чисел кратные M и больше K
k = 100
m = 2
n = 3
counter = 0
while counter < n:
    if counter == n:
        break
    for i in range(k, 1000):
        if i % m == 0 and i > k:
            print(i)
    counter += 1
