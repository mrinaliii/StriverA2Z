def arm(a):
    A = str(a)
    n = len(A)
    total = 0

    for digit in A:
        total += int(digit) ** n

    return total == a
