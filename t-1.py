import math

# def get_nums(a):
#     sum = 0
#     for i in range(a):
#         if i % 3 == 0 or i % 5 == 0:
#             sum += i
#     print(sum)

# get_nums(1000000)

rng = 9999999999999999999999999

def sum_divisible_by(a):
    p = math.floor(rng / a)
    return a * (p*(p+1)) / 2

print(sum_divisible_by(3) + sum_divisible_by(5) - sum_divisible_by(15))