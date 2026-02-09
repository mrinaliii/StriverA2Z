# E
# D E
# C D E
# B C D E
# A B C D E
def pattern(N):
    for i in range(N):
        start = ord('A')+N-1-i
        end = ord('A')+N-1
        for ch in range(start, end+1):
            print(chr(ch),end=" ")
        print()
pattern(5)
