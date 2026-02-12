#TC AND SC: O(d) or O(log n)

import string
def count_digits(n):
    N = str(n)
    return len(N)

print(count_digits(12345))

#TC = O(log n) SC = O(1)

def count_digits(n):
    count = 0
    while n>0:
        count+=1
        n//=10
    return count
print(count_digits(12345))
