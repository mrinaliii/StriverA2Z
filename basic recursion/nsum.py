def nsum(n, tot):
    if n==0:
        return tot
    else:
        tot+=n
        return nsum(n-1, tot)

tot = 0
print(nsum(5, tot))
