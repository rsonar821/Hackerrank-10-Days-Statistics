# Day 4. Geometric Distribution 2

p = 1/3
q = 1-p
n = 5

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    
def nCr(n,r):
    return factorial(n)/(factorial(r) * factorial(n-r))

sum = 0
for i in range (1, n+1):
    sum += (q**(i-1))*p

print(round(sum, 3))