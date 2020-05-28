from itertools import count
from sys import maxsize

def rectangle_count(width, height):
    return (width * (width + 1) * height * (height + 1)) // 4

def test_rectangle_count_example():
    assert rectangle_count(3, 2) == 18

if __name__ == "__main__":
    target = 2 * (10**6)
    closest_difference = maxsize
    area_closest = None

    for width in count(1):
        for height in range(1, width+1):
            count = rectangle_count(width, height)
            difference = abs(target - count)
            if difference < closest_difference:
                closest_difference = difference
                area_closest = width * height
            if count > target + closest_difference:
                if height == 1:
                    # We can stop, all the following grids will have more rectangles
                    print(area_closest)
                    exit()
                else: 
                    # All the following grids with this width will have more rectangles, go to width += 1
                    break