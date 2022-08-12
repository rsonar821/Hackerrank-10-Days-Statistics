# Day 6. Central Limit Theorem 3

import math
n = 100
mean = 500
sd = 80
z = 1.96

print(round(-1.96*(sd/math.sqrt(n))+mean, 2))
print(round(1.96*(sd/math.sqrt(n))+mean, 2))