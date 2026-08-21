lst = list[int](map(int, input("input numbers: ").split()))

def change_site(a, b):
    c = a
    a = b
    b = c
    return a, b

tag = False
ind = 0
while True:
    if ind == len(lst) - 1 and tag == False:
        print(lst)
        break

    if ind == len(lst)-1:
        tag = False
        ind = 0

    if lst[ind] > lst[ind+1]:
        lst[ind], lst[ind+1] = change_site(lst[ind], lst[ind+1])
        tag = True
    ind += 1

