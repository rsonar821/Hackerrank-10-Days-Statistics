# Day 7. Pearson Correlation Coefficient 1

import math
n = int(input())
x = list(map(float, input().split()))
y = list(map(float, input().split()))

x_mean = sum(x)/len(x)
y_mean = sum(y)/len(y)
x_1 = [(i-x_mean)**2 for i in x]
y_1 = [(i-y_mean)**2 for i in y]
x_sd = math.sqrt(sum(x_1)/(len(x_1)))
y_sd = math.sqrt(sum(y_1)/(len(y_1)))

numerator = sum((x[i]-x_mean)*(y[i]-y_mean) for i in range (n))
denominator = n*x_sd*y_sd
result = numerator/denominator
print(round(result, 3))