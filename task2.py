x = input("Input the Filename: ")
n=len(x)
for i in range (1,n):
	if x[i]=='.':
		y=i
print(x[y+1::])

