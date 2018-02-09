MAX = 4 * 1000 * 1000

l = [1, 2]

fib = l[-1] + l[-2]

while fib < MAX:
    l.append(fib)
    fib = l[-1] + l[-2]

print(sum(filter(lambda x: x % 2 is 0, l)))
