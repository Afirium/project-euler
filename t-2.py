def first_solution():
    result, f1, f2 = 0, 1, 2

    while f2 < 4000000:
        if f2 % 2 == 0:
            result += f2
        f1, f2 = f2, f1 + f2

    print(result)


def optimized_solution():
    result, f1, f2 = 0, 1, 1
    f3 = f1 + f2

    while f3 < 4000000:
        result += f3
        f1 = f2 + f3
        f2 = f1 + f3
        f3 = f1 + f2

    print(result)


first_solution()
optimized_solution()
