lst = list(map(int, input().split()))
lst.sort()
order = input()

dic = {'A': lst[0], 'B': lst[1], 'C': lst[2]}

for i in order:
    print(dic[i], end=' ')
