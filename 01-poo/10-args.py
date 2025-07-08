def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total


res1 = add(1, 2, 3)
res2 = add(4, 5, 6)

print(res1)  # Output: 6
print(res2)  # Output: 15
