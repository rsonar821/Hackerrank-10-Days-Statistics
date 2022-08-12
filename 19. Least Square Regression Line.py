# Day 8. Least Square Regression Line

x = [95, 85, 80, 70, 60]
y = [85, 95, 70, 65, 70]
n = len(x)
sum_x = sum(x)
mean_x = sum_x/n
sum_y = sum(y)
mean_y = sum_y/n
x2 = sum([i**2 for i in x])
y2 = sum([i**2 for i in y])
xy = sum([x[i]*y[i] for i in range(n)])

b = ((n*xy)-(sum_x*sum_y))/((n*x2)-(sum_x**2))
a = mean_y-(b*mean_x)
print(a+(b*80))