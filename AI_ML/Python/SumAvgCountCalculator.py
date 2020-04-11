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
numpy_arr=np.array(arr)
print("Sum is ",numpy_arr.sum())
print("Count is ",len(numpy_arr))
print("Average is ", numpy_arr.sum()/len(numpy_arr))
