import numpy as np
arr=[]
while True:
    x=input("Enter a number:")
    if x=='Done':
        print(arr)
        break
    else:
        try:
            float_x=float(x)
            arr.append(float_x)
        except:
            print("Bad number")
min=arr[0]
max=arr[0]
for i in arr :
    if min>i:
        min=i
    if max<i:
        max=i
print("Maximum number is",max)
print("Mininum number is",min)
