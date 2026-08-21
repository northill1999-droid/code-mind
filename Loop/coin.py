n = int(input())

coins = 1
days = 0
salary = 0
while days < n:
    for _ in range(coins):
        salary += coins
        days += 1
        if days == n:
            break
    
    coins += 1

print(salary)
