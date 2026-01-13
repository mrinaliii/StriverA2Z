# 1        1
# 12      21
# 123    321
# 1234  4321
# 1234554321
def pattern(rows):
    space=2*(rows-1)
    for i in range(1,rows+1):
        for j in range(1,i+1,1):
            print(j,end="")
        print(" "*space, end="")
        for j in range(i,0,-1):
            print(j, end="")
        print()
        space-=2
pattern(5)
