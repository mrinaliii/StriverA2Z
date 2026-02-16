def prno(n, count):
    if count==n+1:
        return
    else:
        print(count)
        prno(n, count+1)
count=1
prno(10,count)
