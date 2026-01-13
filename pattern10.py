# 1
# 01
# 101
# 0101
# 10101
def pattern(rows):
    for i in range(rows):
        if i%2==0:
            start=1
        else:
            start=0
        for j in range(i+1):
            print(start, end="")
            start=1-start
        print()
pattern(5)
