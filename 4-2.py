text = input()
res = {letter: text.count(letter) for letter in text}
print(res)
