# Day 4: Binomial Distribution 1

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    
def nCr(n,r):
    return factorial(n)/(factorial(r) * factorial(n-r))

p = 1.09/(1.09+1)
q = 1-p

sum=0
for i in range(3,7):
    temp = nCr(6,i)
    temp1 = (p**i)*(q**(6-i))
    sum += temp*temp1
print(round(sum, 3)) 