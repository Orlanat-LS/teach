def f(n):
    if n == 1:
        return 1
    else:
        return f(n - 1) + n

res = f(3)
print(res)


def IsPalindrome(S):
    if len(S) <= 1:
        return True
    else:
        return S[0] == S[-1] and IsPalindrome(S[1:-1])

def f(n):
    if n == 1:
        return 1
    else:
        return f(n-1) - g(n-1)

def g(n):
    if n == 1:
        return 1
    else:
        return f(n-1) + 2 * g(n-1)

print(f(5)/g(5))