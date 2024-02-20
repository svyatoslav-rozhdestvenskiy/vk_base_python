text = input().lower().split()
word_dict = {}
for word in text:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1
max_count = 0
result = None
for key, value in word_dict.items():
    if max_count < value:
        max_count = value
        result = f'{key} {value}'
print(result)
