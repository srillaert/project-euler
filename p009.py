for c in range(334, 999):
    b_range_start = (1000 - c) // 2 + 1 # a < b
    b_range_stop = 1000 - c if c > 500 else c # b < c
    for b in range(b_range_start, b_range_stop):
        a = 1000 - b - c
        if a*a + b*b == c*c:
            print(a*b*c)
            exit()