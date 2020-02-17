sum = 0
with open("p013.input") as input_file:
    for line in input_file.readlines():
        number = int(line)
        sum += number
result = str(sum)[0:10]
print(result)
