isnb = input()

lst = []
for i in isnb[:-1:]:
    if i.isdigit():
        lst.append(int(i))

pre_num = 0
for i in range(1, 10):
    pre_num += lst[i-1] * i
mod_result = pre_num % 11

ident_code = str(mod_result)
if mod_result == 10:
    ident_code = 'X'

if ident_code == isnb[12::]:
    print("Right")
else:
    print(isnb[:-1]+ident_code)