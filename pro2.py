n=int(input("Enter the size of the array: "))
a=[]
for i in range(n):
    x=input("enter the element of array: ")
    a.append(x)
for i in range(0,n-1):
    a[i]=max(a[i+1:])
print("Final array is:", a)