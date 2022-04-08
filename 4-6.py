list_1 = [1, 5, 6, 11, 2, 3]
list_1.sort()
print(list_1)
elem_end = list_1.pop(-1)
elem1 = list_1.pop(0)
list_1.insert(0, elem_end)
list_1.append(elem1)
print(list_1)
