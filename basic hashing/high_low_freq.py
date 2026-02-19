#Problem Statement: Problem Statement: Given an array of size N. Find the highest and lowest frequency element.


from collections import defaultdict

def hlfreq(arr):
    d = defaultdict(int)
    for i in arr:
        d[i]+=1
    mx = max(d.values())
    mn = min(d.values())
    for k,v in d.items():
        if v==mx:
            print("Highest occurences are of: ", k)
        if v==mn:
            print("Lowest occurences are of: ", k)
arr = [10,5,10,15,10,5]
hlfreq(arr)
