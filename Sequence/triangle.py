s = input("please input a char: ")

space, char_cnt = 2, 1
for i in range(1, 4):
    print(" " * space + s * char_cnt)
    space -= 1
    char_cnt += 2
