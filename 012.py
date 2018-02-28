import math

def triangle(num):
    return num * (num + 1) / 2

def count_devisors(num):
    res = 0
    for i in range(1, int(math.sqrt(num))):
        if num % i == 0:
            res += 2

    return res

num = 2
while(count_devisors(triangle(num)) < 500):
    num += 1

print(triangle(num))
