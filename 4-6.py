# list_1 = [1, 5, 6, 11, 2, 3]
# a = max(list_1)
# b = min(list_1)
# list_1.insert(list_1.index(a), b)
# del list_1[list_1.index(a)]
# list_1.insert(list_1.index(b), a)
# del list_1[list_1.index(b)]
# print(list_1)
list_1 = [1, 5, 6, 11, 2, 3]
max_number = max(list_1)
min_number = min(list_1)
max_i = list_1.index(max_number)
min_i = list_1.index(min_number)
list_1[max_i], list_1[min_i] = list_1[min_i], list_1[max_i]
print(list_1)
