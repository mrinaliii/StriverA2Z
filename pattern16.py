def pattern(N):
    for i in range(N):
        print(" " * (N - 1 - i), end="")

        start = ord('A')
        mid = (2*i+1)//2

        for j in range(2 * i + 1):
            print(chr(start), end="")
            if j < mid:
                start += 1
            else:
                start -= 1

        print()

N = 5
pattern(N)
