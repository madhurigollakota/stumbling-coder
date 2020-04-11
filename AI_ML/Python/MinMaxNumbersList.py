numbers=[]
while True:
    x=input("Enter a number :")
    if x=='Done':
        break
    else :
        try:
            numbers.append(float(x))
        except:
            print("enter a valid number")
print(numbers)

print("Maximum number is",max(numbers),'\n',"Minimum number is",min(numbers))
