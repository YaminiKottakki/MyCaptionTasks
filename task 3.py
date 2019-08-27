def largest (lst):
    c=0
    i=0
    n=len(lst)
    while i<n:
        if len(lst[i])>c:
            c=len(lst[i])
            s=lst[i]
            i=i+1
    return(s)
lst=["vizag","chennai","hyderbad"]
x=largest(lst)
print(x)