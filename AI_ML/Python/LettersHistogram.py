import string
x=input("Enter file name:")
try:
    fhandle=open(x,'r')
except:
    print("Bad File name")
    quit()
Hist={}
for line in fhandle:
    line=line.strip()
    line=line.translate(line.maketrans("","",string.punctuation+'0123456789'))
    for i in line:
        if i.isspace()==True:
            continue
        Hist[i.lower()]=Hist.get(i.lower(),0)+1

#To print the output in the order of keys
x=list(Hist.keys())
x.sort()
for l in x:
    print(l,":",Hist[l])
print('\n')
#To print the output in the order of values
k=sorted([(val,key) for key,val in Hist.items()],reverse=True)
for l,m in k:
    print(m,":",l)

#To find the letter with maximum no of count
bigCountLetter=None
bigCount=None
for a,b in Hist.items():
        if bigCount is None or bigCount<b:
            bigCount=b
            bigCountLetter=a
print("Letter with maximum count is ",bigCountLetter," and it appeared",bigCount,"times")
