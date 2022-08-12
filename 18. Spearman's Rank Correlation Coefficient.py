# Day 7. Spearman's Rank Correlation Coefficient

n= int(input())
x= list(map(float, input().split()))
y= list(map(float, input().split()))
            
def srcc(x,y):
    
    x_sort=sorted(x)
    y_sort=sorted(y)
    rank_x={}
    rank_y={}
    for i in x_sort:
        rank_x[i]= x_sort.index(i)+1
        
    for i in y_sort:
        rank_y[i]= y_sort.index(i)+1
        
    length= len(x)         
    d=[]
    for i in range(length):
        temp=rank_x[x[i]]- rank_y[y[i]]
        d.append(temp**2)
                 
    numerator = 6*sum(d)
    denominator = length * ((length ** 2 ) -1)         
        
    return round(1-(numerator/float(denominator)),3)
       
print(srcc(x,y))