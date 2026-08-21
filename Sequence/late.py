import math

s, v = map(int, input().split())

walk_time = math.ceil(s/v)
total_time = walk_time + 10

depart_time = 8 * 60 - total_time

if depart_time < 0:
    depart_time = 60 * 24

h = depart_time // 60
m = depart_time % 60

print(f"{h:02d}:{m:02d}")