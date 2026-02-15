# def gcd(a,b):
#     m = min(a,b)
#     for i in range(m, 0, -1):
#         if a%i==0 and b%i==0:
#             return i

# print(gcd(9,12))


#USING EUCLID
def gcd(a,b):
    while b:
        a,b = b, a%b
    return a
print(gcd(20,15))
