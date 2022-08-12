# Day 6. Central Limit Theorem 1

import math
total = 9800
n = 49
mean = 205
sd = 15

new_mean=n*mean
new_sd=(math.sqrt(n))*sd     
print(round(0.5*(1+math.erf((total-new_mean)/(new_sd*(2**0.5)))),4))