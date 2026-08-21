lst = list[int](map(int, input().split()))

consecutive = 1
result = 1
for i in range(len(lst)-1):
    if lst[i+1] == lst[i] + 1:
        consecutive += 1
        if result < consecutive:
            result = consecutive
        continue

    consecutive = 1

print(result)
