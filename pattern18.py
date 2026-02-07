def pattern(rows):
    print("*" * (2*rows - 1))
    for i in range(1, rows):
        print(
            "*" * (rows - i) +
            " " * (2*i - 1) +
            "*" * (rows - i)
        )
    for i in range(rows - 1, 0, -1):
        print(
            "*" * (rows - i) +
            " " * (2*i - 1) +
            "*" * (rows - i)
        )
    print("*" * (2*rows - 1))

pattern(5)
