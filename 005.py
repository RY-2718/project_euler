import sys

def can_divise(num):
    divisors = [7, 11, 13, 16, 17, 18, 19, 20]
    for i in divisors:
        if num % i != 0:
            return False
    return True

num = 0
while 1:
    num += 20
    if can_divise(num):
        print(num)
        sys.exit(0)
