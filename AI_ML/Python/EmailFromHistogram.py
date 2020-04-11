x=input("Enter a filename:")
try:
    fhandle=open(x,'r')
except:
    pritn("Not a valid file")
    quit()

Senders=dict()
#Creating a dictionary with email id and the count of emails received on the day
for l in fhandle:
    l.strip()
    if l.startswith('From') and not(l.startswith('From:')) :
        Senders[l.split()[1]]=Senders.get(l.split()[1],0)+1

#Using for loop and without sorted function, Fetching the email id from which maximum emails were received
maxCount=None
maxMail=None
for a,b in Senders.items():
    if (maxCount is None) or (maxCount<b):
        maxCount=b
        maxMail=a
print(maxMail,maxCount)

#Using Tuples to sort the dictionary and to find the email id from which maximum emails were received
l=list()
for id,value in Senders.items():
    l.append((value,id))
l=sorted(l,reverse=True)[0]
x,y=l
print(y,x)

#The above code can also be written as follows
z=sorted([(key,value) for value,key in Senders.items()],reverse=True)
i,j=z[0]
print(j,i)
