def average(string_of_numbers: str):
    list_of_numbers = list(map(int, string_of_numbers.split()))
    result = 0
    for number in list_of_numbers:
        result += number
    result = result / len(list_of_numbers)
    result = round(result, 2)
    return result


result = []
while data := input():
    result.append(average(data))
for i in range(len(result)):
    print(result[i])
