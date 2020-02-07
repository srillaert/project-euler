largest_palindrome = 0
start = 999
end = 99

for a in range(start,end,-1):
    for b in range(start,a,-1):
        product = a * b
        if product <= largest_palindrome:
            break
        string = str(product)
        if string == string[::-1]:
            #print("a = " + str(a) + ", b = " + str(b) + ", product = " + string)
            largest_palindrome = product

print(largest_palindrome)
