def number_of_ways(total):
    counts = [1] * (total + 1)
    for coin in [2, 5, 10, 20, 50, 100, 200]:
        for i in range(coin, total+1):
            counts[i] += counts[i-coin]
    return counts[total]

print(number_of_ways(200))