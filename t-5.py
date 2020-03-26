max = [0, 0, 0]

for j in range(100, 1000):
    for i in range(100, 1000):
        n = i * j
        if str(n) == str(n)[::-1] and n > max[0]:
            max = [n, i, j]

print(max)
