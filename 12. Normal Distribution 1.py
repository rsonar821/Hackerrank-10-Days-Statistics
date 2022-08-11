# Day 5. Normal Distribution 1

import math
mean = 20
std = 2

def normal_distribution(x, mean, std):
    pro = 0.5*(1+math.erf((x-mean)/(std*(2**0.5))))
    return round(pro, 3)

print(normal_distribution(19.5, mean, std))
pro1 = normal_distribution(22, mean, std)
pro2 = normal_distribution(20, mean, std)
print(pro1-pro2)
