#roblem Statement: Given an array, we have found the number of occurrences of each element in the array.
from collections import defaultdict
def freq(arr):
    d=defaultdict(int)
    for i in arr:
        d[i]+=1
    for x,y in d.items():
        print("No. of ",x," = ",y)

arr = [10,5,10,15,10,5]
freq(arr)
