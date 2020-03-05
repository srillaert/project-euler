one_to_nine = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
ten_to_nineteen = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens_from_twenty_to_ninety = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def get_numbers_below_100():
    for d in one_to_nine:
        yield d
    for n in ten_to_nineteen:
        yield n
    for ten in tens_from_twenty_to_ninety:
        yield ten
        prefix = ten + "-"
        for d in one_to_nine:
            yield prefix + d

def get_numbers():
    for n in get_numbers_below_100():
        yield n
    for digit in one_to_nine:
        hundred = digit + " hundred"
        yield hundred
        prefix = hundred + " and "
        for number_below_100 in get_numbers_below_100():
            yield prefix + number_below_100
    yield "one thousand"

sum = 0
#i = 1
for number in get_numbers():
    length = len(number.replace(" ", "").replace("-", ""))
    sum += length
    #print(i, number, length, sum)
    #i += 1
print(sum)
