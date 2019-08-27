input("enter values")
a=int(input())
b=int(input())
c=int(input())
if a==b and b==c and c==a:
    print("equilater triangle")
elif a==b or a==c or b==c:
    print("isoscale triangle")
else:
    print("scalene triangle")  