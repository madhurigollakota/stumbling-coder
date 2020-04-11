x=input("Enter file name:")
try:
    fhandle=open(x,'r')
except:
    print("Bad filename")
    quit()
count=0

for line in fhandle:
    if line.startswith('From') and not(line.startswith("From:")):
            print(line.split()[1])
            count=count+1

print("There were ",count," number of files with from as the first word")
