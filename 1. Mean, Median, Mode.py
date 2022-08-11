# Day 0: Mean, Median and Mode

from scipy import stats
n = int(input())
lst = list(map(int, input().strip().split()))
lst = sorted(lst)

print(sum(lst)/len(lst))

if len(lst)%2 == 0:
    n1 = int((len(lst)/2)-1)
    n2 = int(len(lst)/2)
    median = (lst[n1]+lst[n2])/2
else:
    n3 = len(lst)//2
    median = lst[n3]
print(median)

print(stats.mode(lst)[0][0])