n, x = map(int, input().split())

cnt = 0
# for i in range(1, n+1):
#     for j in str(i):
#         if j == str(x):
#             cnt += 1

# print(cnt)

for i in range(1, n+1):
    while i > 0:
        num = i % 10

        if num == x:
            cnt += 1
        i = i // 10

print(cnt)
