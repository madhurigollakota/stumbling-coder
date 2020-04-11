hours=input("Enter Hours :")
rate=input("Enter Rate :")

try :
    hours_float=float(hours)
    rate_float=float(rate)
except :
    print("Error, Please enter a numeric input")
    quit()
def computepay(hours,rate):
    if hours_float>40 :
        return str(round((40*rate)+((hours-40)*rate*1.5),2))
    else :
        return str(round(hours*rate,2))

print("Pay :",computepay(hours_float,rate_float))
