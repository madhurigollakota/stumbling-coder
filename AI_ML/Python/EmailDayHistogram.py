x=input("Enter a filename")
try:
    fhandle=open(x,'r')
except:
    pritn("Not a valid file")
    quit()

Days=dict()
for l in fhandle:
    l.strip()
    if l.startswith('From') and not(l.startswith('From:')) :
        Days[l.split()[2]]=Days.get(l.split()[2],0)+1
print(Days)
