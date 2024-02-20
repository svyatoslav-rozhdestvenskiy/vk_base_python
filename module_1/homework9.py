text = input().lower()
unique_chars = set(text)
unique_chars.discard(' ')
unique_chars = list(unique_chars)
unique_chars.sort()
print(" ".join(unique_chars))

