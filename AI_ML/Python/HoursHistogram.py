x=input("Enter a filename:")
try:
    fhandle=open(x,'r')
except:
    pritn("Not a valid file")
    quit()

Hours=dict()
#Creating a dictionary of hours and count of mails recived at that hour
for line in fhandle:
    line.strip()
    if line.startswith('From') and not(line.startswith('From:')):
        line=line.split()[5]
        line=line.split(':')[0]
        Hours[line]=Hours.get(line,0)+1
#Sorting the dictionary
x=sorted(Hours.items())
for l,m in x:
    print(l,m)
