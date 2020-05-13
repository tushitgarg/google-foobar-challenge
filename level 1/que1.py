def solve(x,y):
    if(len(x)>len(y)):
        z = list(set(x)-set(y))
    else:
        z = list(set(y)-set(x))
    return z[0]
        
    
x = [14,27,1,4,2,50,3,1]
y = [2,4,-4,3,1,1,14,27,50]
print(solve(x,y))