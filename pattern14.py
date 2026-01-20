# A B C D E
# A B C D
# A B C
# A B
# A
def pattern(N):
    for i in range(N, 0, -1):
        start=ord('A')
        for j in range(start, start+i):
            print(chr(j), end=" ")
        print()
N=5
pattern(5)
