import math
import sys

def makePalindromicNumber(input):
    input = str(input)
    return int(input + input[::-1])

origin = 999
while origin >= 100:
    num = makePalindromicNumber(origin)
    for i in range(100, int(math.sqrt(num))):
        if num % i == 0 and num / i >= 100 and num / i <= 999:
            print(num, i, num / i)
            sys.exit(0)
    origin -= 1
