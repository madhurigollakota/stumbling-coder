x=int(input("Enter number:"))
sum=0
for i in range(x) :
    if i%3==0 or i%5==0 :
        sum=sum+i
print(sum)
