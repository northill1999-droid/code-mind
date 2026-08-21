def square(n):
    num = 0
    for _ in range(n):
        for _ in range(n):
            num += 1
            if num < 10:
                print('0'+str(num), end='')
                continue
            print(str(num), end='')
        print()

def triangle(n):
    num = 0
    space_cnt = 2*n - 2
    num_cnt = 1
    for _ in range(n):
        for _ in range(space_cnt):
            print(' ', end='')

        for _ in range(num_cnt):
            num += 1
            if num < 10:
                print('0'+str(num), end='')
                continue
            print(str(num), end='')

        print()
        num_cnt += 1
        space_cnt -= 2

if __name__ == "__main__":
    # square(4)
    triangle(9)
    