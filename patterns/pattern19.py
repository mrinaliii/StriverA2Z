# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *
def pattern(N):
    sp = 2*N-2
    for i in range(1, 2*N):
        if i<=N:
            stars=i
        else:
            stars=2*N-i
        print("*"*stars, end="")
        print(" "*sp, end="")
        print("*"*stars, end="")
        if i<N:
            sp-=2
        else:
            sp+=2
        print()
pattern(5)
