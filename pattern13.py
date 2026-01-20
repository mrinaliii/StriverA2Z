# A
# A B
# A B C
# A B C D
# A B C D E
def pattern(N):
    for i in range(N):
        start = ord('A')
        for j in range(start, start+i+1):
            print(chr(j),end=" ")
        print()

N = 5
pattern(N)
