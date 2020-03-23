result, f1, f2 = 0, 1, 2

while f2 < 4000000:
    if f2 % 2 == 0:
        result += f2
    f1, f2 = f2, f1 + f2

print(result)
