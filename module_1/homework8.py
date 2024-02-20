number_of_experiments = int(input())
experiments = []
try:
    while data := list(map(int, input().split())):
        experiments.append(data)
except EOFError:
    pass
result = []
for i in range(number_of_experiments):
    result.append(max(experiments[i]))
result.sort(reverse=True)
result = list(map(str, result))
result = ';'.join(result)
print(result)
