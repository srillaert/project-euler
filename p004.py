largest = 0
start = 100
end = 1000

for a in range(start,end):
    for b in range(a,end):
        number = a * b
        string = str(number)
        if string == string[::-1]:
            if number > largest:
                #print("a = " + str(a) + ", b = " + str(b) + ", number = " + string)
                largest = number

print(largest)
