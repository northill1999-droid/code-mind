n = int(input())

cnt = n
num = 0
for i in range(n):
    for j in range(cnt):
        num += 1
        if num < 10:
            print("0"+str(num), end='')
            continue
        print(num, end='')
    print()
    cnt -= 1
