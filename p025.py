number_of_digits = 1000
minimum_number = 10 ** (number_of_digits - 1)

previous = 1
current = 1
index = 2
while current < minimum_number:
    fibon = previous + current
    previous = current
    current = fibon
    index += 1 

print(index)
