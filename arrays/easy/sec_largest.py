arr = [1, 2, 4, 7, 7, 5]
arr.sort()
if arr[0]==arr[1]:
    print("Second smallest element is: ",arr[2])
if arr[-1]==arr[-2]:
    print("Second largest element is: ", arr[-3])
else:
    print("Second smallest element is: ",arr[1])
    print("Second largest element is: ", arr[-2])
