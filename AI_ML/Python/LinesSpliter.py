fname=input("Enter a filename:")
try:
    fhandle=open(fname,'r')
except:
    print("Bad file name")
    quit()
words=[]
for line in fhandle:
     for word in line.split():
            if word in words:
                continue
            else:
                words.append(word)
words.sort()
print(words)
