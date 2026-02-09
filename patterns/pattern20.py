# *****
# *   *
# *   *
# *   *
# *****
def pattern(N):
    print("*"*N)
    for i in range(N-2):
        print("*",end="")
        print(" "*(N-2),end="")
        print("*")
    print("*"*N)
pattern(6)
