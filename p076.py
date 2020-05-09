def number_of_ways(sum):
    counts = [1] * (sum + 1)
    for i in range(2, sum):
        for j in range(i, sum+1):
            counts[j] += counts[j-i]
    return counts[sum]

print(number_of_ways(100))