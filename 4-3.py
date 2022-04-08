import collections
n = int(input())
name = input('name ')
mail = input('mail ')
dict_1 = {name, mail}
defdict = collections.defaultdict(list)
for i in range(0, n):
    defdict[i].append(dict_1)
print(defdict)
