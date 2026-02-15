import math
def div(a):
    for i in range(1, int(math.sqrt(a))+1):
        if a%i==0:
            print(i)
            if i!=a//i:
                print(a//i)
div(36)
