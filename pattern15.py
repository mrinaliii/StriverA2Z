# A
# BB
# CCC
# DDDD
# EEEEE
def pattern(N):
    start=ord('A')
    for i in range(1, N+1):
        print(chr(start)*i, end=" ")
        start+=1
        print()
N=5
pattern(N)
