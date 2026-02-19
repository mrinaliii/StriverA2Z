def palindrome(s):
    n = len(s)
    for i in range(n//2):
            if s[i]!=s[n-i-1]:
                return False
    return True
#or simply return s==s[::-1]
s="ABCDCBA"
print("Palindrome") if palindrome(s) else print("Not Palindrome")
