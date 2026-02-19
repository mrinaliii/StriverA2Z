from collections import deque

def sr(arr):
    temp = sorted(arr)
    arr = deque(arr)
    x = 0
    while x!=len(arr):
        arr.rotate(-1)
        if list(arr)==temp:
            return True
        else:
            x+=1
    return False

arr=[3,4,5,1,2]
print(sr(arr))
