# Day 5. Poisson Distribution 1

lam = 2.5
k = 5 

num = (lam**k)*((2.71828)**(-lam))
den = 5*4*3*2
probability = num/den
print(round(probability, 3))
