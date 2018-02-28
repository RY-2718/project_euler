import sys

for c in range(int(1000 / 3) + 1, int(1000 / 2) - 1):
    a = 1000 - 2 * c + 1
    b = c - 1
    while a <= b:
        if a * a + b * b == c * c:
            print(a, b, c, a * b * c)
            sys.exit(0)
        a += 1
        b -= 1
