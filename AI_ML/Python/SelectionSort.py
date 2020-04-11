#In every iteration of selection sort,
#the minimum element (considering ascending order) from the unsorted subarray is picked
#and moved to the sorted subarray.

x=[3,90,21,57,45,8,34,58]
print("Before",x)

def selectionSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i]<arr[j]:
               arr[i],arr[j]=arr[j],arr[i]
    return(arr)

print("After :",selectionSort(x))
