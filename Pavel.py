# Внести первые N чисел кратные M и больше K
k = 100
m = 2
n = 3
i = 0
while i < n:
    for i in range(k, ):
        if i % m == 0 and i > k:
            i += 1
            print(i)
