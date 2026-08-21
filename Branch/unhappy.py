lst = []

for _ in range(7):
    lst.append(sum(list(map(int, input().split()))))

lst1 = []
max1 = lst[0]
for i in range(len(lst)):
    if lst[i] > max1:
        max1 = lst[i]

for i in range(len(lst)):
    if lst[i] == max1:
        print(f"unhappy day is {i+1}")
        break