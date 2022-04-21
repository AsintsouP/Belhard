# Дан список чисел и на вход поступает число N, необходимо сместить список на
# указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]

def sdvig(lst: list, n: int) -> list:
    if n > 0:
        return lst[-n:] + lst[:-n]
    elif n < 0:
        return lst[-n:] + lst[:-n]
    else:
        return lst

lst = [1, 2, 3, 4, 5, 6, 7]
n = -2
print(sdvig(lst, n))