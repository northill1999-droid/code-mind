a, b, c, d = map(int, input().split())

minu1 = a * 60 + b
minu2 = c * 60 + d

swim_time = minu2 - minu1

time_hour = swim_time // 60
time_minu = swim_time % 60
# print(time_hour, time_minu)

hour_real = time_hour + a
minu_real = time_minu + b
if minu_real >= 60:
    hour_real += 1
    minu_real -= 60

print(hour_real, minu_real)