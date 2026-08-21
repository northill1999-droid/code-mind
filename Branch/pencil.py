n = int(input())
lst = []
for _ in range(3):
    lst.append(list[int](map(int, input().split())))

final_cost = 0
for i in lst:
    cnt = 0
    pencil_count = 0
    consumption = 0
    while pencil_count < n:
        cnt += 1
        pencil_count = cnt * i[0]
        consumption = cnt * i[1]
    
    if consumption < final_cost:
        final_cost = consumption
        continue
    final_cost = consumption
    
print(final_cost)