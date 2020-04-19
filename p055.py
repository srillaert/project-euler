result = 0
for number in range(1, 10000):
    str_number = str(number)
    str_reverse = str_number[::-1]
    for iterations in range(1, 51):
        number += int(str_reverse)
        str_number = str(number)
        str_reverse = str_number[::-1]
        if str_number == str_reverse:
            break # palindromic
    if iterations == 50:
        result += 1
print(result)