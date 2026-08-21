a_speed = 5
b_speed = 8

gap = 100

time = 0
while gap > 0:
    gap = gap - (b_speed - a_speed)
    time += 1

print(time)