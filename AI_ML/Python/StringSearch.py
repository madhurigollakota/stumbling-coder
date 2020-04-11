str = 'X-DSPAM-Confidence: 0.8475 '
x=str.find(":")
num=str[x+1:]
float_num=float(num.strip())
print(float_num)
