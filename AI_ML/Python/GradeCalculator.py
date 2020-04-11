x=input("Enter score:")
try:
    intx=float(x)
except:
    intx=-1
def computescore(score):
    if score>=0 and score<=1 :
        if score>=0.9 :
            return "A"
        elif score>=0.8 :
            return "B"
        elif score>=0.7 :
            return "C"
        elif score>=0.6 :
            return "D"
        else :
            return "F"
    else :
        return "Bad Score"
print(computescore(intx))
