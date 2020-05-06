from itertools import count

lookup = {}
for number in count(1):
    cube = number ** 3
    key = "".join(sorted(str(cube)))
    count, smallest_cube = lookup.get(key, (0, cube))
    if count >= 4:
        print(smallest_cube)
        break
    lookup[key] = (count + 1, smallest_cube)