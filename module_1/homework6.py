text = input()
count = 0
result = text.lower()
for char in text:
    if char == '!':
        result = result.replace('!', '', 1)
        count += 1
    if char == '#':
        result = result.replace('#', '', 1)
        count += 1
    if char == '%':
        result = result.replace('%', '', 1)
        count += 1
    if char == '@':
        result = result.replace('@', '', 1)
        count += 1
print(count)
print(result)
