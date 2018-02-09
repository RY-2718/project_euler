from functools import reduce

print(reduce(lambda x, y: x + y, filter(lambda x: x % 3 is 0 or x % 5 is 0, range(1,1000))))
