# numbers = '4 5 6 7 4 5 6 7'
# numbers = numbers.split(' ')
# for i, number in enumerate(numbers):
#     numbers[i] = int(number)
# print(numbers)

text = input()
for i, elem in enumerate(text):
    if not i % 2:
        print(text)
for i in range(0, len(text), 2):
        print(text[i])


# reserved_number = 0
# tmp_original = number
# while tmp_original > 0:
#     reserved_number = (reserved_number * 10) + tmp_original % 10
#     tmp_original = tmp_original // 10
#
# if number == reserved_number:
#     print('Palindrome')
# else:
#     print('No Palindrome')