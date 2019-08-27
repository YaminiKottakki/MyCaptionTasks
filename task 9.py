lst=[10,21,32,6,81]
n=len(lst)
ce=0
cod=0
for i in range(0,n):
    
    if lst[i]%2==0:
        ce=ce+1
     
    else:
        cod=cod+1
        
print(ce,",",cod)
