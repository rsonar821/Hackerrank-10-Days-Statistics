# Day 6. Central Limit Theorem 2

import math
total = 250
n = 100
mean = 2.4
sd = 2.0

new_mean=n*mean
new_sd=(math.sqrt(n))*sd     
print(round(0.5*(1+math.erf((total-new_mean)/(new_sd*(2**0.5)))),4))