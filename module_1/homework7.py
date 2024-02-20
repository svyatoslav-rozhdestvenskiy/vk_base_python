text_list = input().split()
print(round(sum(len(el) for el in text_list) / len(text_list), 2))
