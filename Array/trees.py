l, n = map(int, input().split())
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))


tree = [1] * (l+1)
for i in lst:
    for ind in range(i[0], i[1]+1):
        tree[ind] = 0

print(sum(tree))