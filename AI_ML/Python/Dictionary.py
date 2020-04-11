import string as s
x=input("Enter a file name:")
try:
    fhandle=open(x,'r')
    fhandle2=open(x,'r')
except:
    print("Bad filename")
    quit()
catalog={}
for line in fhandle:
    line=line.lower()
    line=line.translate(line.maketrans("","",s.punctuation))
    for words in line.split():
        if words in catalog:
            catalog[words]=catalog[words]+1
        else:
             catalog[words]=1
for key in catalog:
    print(key,catalog[key])
#print('\n')
#The above lines of code can also be written as follows
#catalog2={}
#for h in fhandle2:
#    h=h.lower()
#    h=h.translate(h.maketrans("","",s.punctuation))
#    for i in h.split():
#        catalog2[i]=catalog2.get(i,0)+1
#for key2 in catalog2:
#    print(key2,catalog[key2])
