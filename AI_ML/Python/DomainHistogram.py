x=input("Enter a filename:")
try:
    fhandle=open(x,'r')
except:
    pritn("Not a valid file")
    quit()

Domains=dict()
for l in fhandle:
    l.strip()
    if l.startswith('From') and not(l.startswith('From:')) :
        l=l.split()[1]
        l=l.split('@')[1]
        Domains[l]=Domains.get(l,0)+1

print(Domains)
maxCount=None
maxMail=None
for a,b in Domains.items():
    if (maxCount is None) or (maxCount<b):
        maxCount=b
        maxMail=a
print(maxMail,maxCount)
