from itertools import count, islice

def e_sequence():
    yield 1
    yield 2
    for i in count(4, 2):
        yield 1
        yield 1
        yield i

numerator, denominator = 0, 1
sequence = list(islice(e_sequence(), 99))
for x in reversed(sequence):
    numerator, denominator = (denominator, x * denominator + numerator)
result = sum(map(int, str(2 * denominator + numerator)))
print(result)