length = 13
with open("p008.input") as input_file:
    line = input_file.read().replace("\n", "")

greatest_product = 0

for i in range(length,1000-length):
    product = 1
    for j in range(0,length):
        product *= int(line[i+j])
    if product > greatest_product:
        greatest_product = product

print(greatest_product)
