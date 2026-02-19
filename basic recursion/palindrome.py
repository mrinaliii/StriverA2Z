def palindrome(s):
    n = len(s)
    for i in range(n//2):
            if s[i]!=s[n-i-1]:
                return False
    return True
#or simply return s==s[::-1]
s="ABCDCBA"
print("Palindrome") if palindrome(s) else print("Not Palindrome")


def isPalindrome(self, s):
        left = 0
        right = len(s)-1
        while right>left:
            if not s[left].isalnum():   left+=1
            elif not s[right].isalnum():  right-=1
            else:
                if s[left].lower()!=s[right].lower():   return False
                left+=1
                right-=1
        return True
