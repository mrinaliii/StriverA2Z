def fib(n):
    if n<=1:
        return n
    l = fib(n-1)
    sl = fib(n-2)
    return l+sl
print(fib(5))


def fib(self, n, memo={}):
    if n in memo:
        return memo[n]
    if n<=1:
        return n
    memo[n]=self.fib(n-1,memo)+self.fib(n-2,memo)
    return memo[n]
