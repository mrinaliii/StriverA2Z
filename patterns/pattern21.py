# 444444
# 433333
# 432223
# 432123
# 432223
# 433333
def pattern(N):
    for i in range(2*N-2):
        for j in range(2*N-2):
            t = i
            l = (2*N-2)-i
            b = j
            r = (2*N-2)-j
            m = min(t,l,b,r)
            print(N-m,end="")
        print()
pattern(4)
