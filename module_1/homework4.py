text = input()
result = False
for char in text:
    if char == 'a' or char == 'o':
        result = True
    if char == 'i' or char == 'e':
        result = False
        break
print(result)
