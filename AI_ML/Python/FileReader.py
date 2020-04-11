try:
    name=input("Enter a file name: ")
    handle=open(name)
except:
    print("Enter a valid file name")
    quit()
count=0
sum=0
for line in handle:
    #print((line.rstrip()).upper())
    if line.startswith("X-DSPAM-Confidence:"):
        num=float(line[(line.find(":")+1):].strip())
        count=count+1
        sum=sum+num
print("Sum is ",sum," and count is ",count)
print("Average spam confidence:",sum/count)
