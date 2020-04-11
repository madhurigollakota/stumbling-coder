x=[3,90,21,57,45,8,34,58]
print("Before",x)

def bubblesort(arr) :
    n=len(arr)
    for i in range(n):
            for j in range(n-i-1):
               if arr[j]>arr[j+1]:
                   arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

print("After",bubblesort(x))
