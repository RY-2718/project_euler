import math

# sum(k^2) = 1/6 * n(n+1)(2n+1)
sum_of_square = 100 * (100 + 1) * (2 * 100 + 1) / 6

# sum(k) = 1/2 * n(n+1)
square_of_sum = math.pow(100 * (100 + 1) / 2, 2)

print(square_of_sum - sum_of_square)
