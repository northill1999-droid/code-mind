def reverse_num(n):
    sign = -1 if n < 0 else 1
    n = abs(n)

    rev_num = 0
    while n > 0:
        left = n % 10
        rev_num = rev_num*10 + left
        n = n // 10
    return sign * rev_num

def palindromic(n):
    if n == reverse_num(n):
        return True
    return False

def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    a, b = map(int, input().split())

    for i in range(a, b+1):
        if prime(i) and palindromic(i):
            print(i, end=' ')
    