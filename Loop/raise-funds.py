n = int(input())
w = n // 364

k = max(1, (w - 100 + 2) // 3)
x = w - 3*k

print(x, k)