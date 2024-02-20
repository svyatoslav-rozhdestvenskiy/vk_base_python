text = input().lower()
remove_chars = ['!', '.', ',', ':', ';', '?', '#', '$', '%', '^', '&', '*', '(', ')']
for char in remove_chars:
    text = text.replace(char, '')
text = text.split()
result_dict = {}
result_list = []
for word in text:
    if len(word) >= 5:
        word_set = set(word)
        if len(word_set) >= 4:
            if word in result_dict:
                result_dict[word] += 1
            else:
                result_dict[word] = 1
for key, value in result_dict.items():
    if value > 2:
        result_list.append(key)
result_list.sort()
for word in result_list:
    print(word)
