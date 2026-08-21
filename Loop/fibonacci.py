n = int(input())

a = 1
b = 1
lst = [a, b]
for i in range(n-2):
    if n == 1 or n == 2:
        print(1)
        break

    next_one = a + b
    a = b
    b = next_one
    lst.append(next_one)

# print(f"list: {lst}, lenght: {len(lst)}")
print(f"{next_one:.2f}")
