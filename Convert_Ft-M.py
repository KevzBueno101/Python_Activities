#Ft - M conversion 
#1ft = 0.3048m
#M= ft.* 0.3048

#define formula for calculating ft -m
def cal(ft):
    return ft * 0.3048
#input
ft = float(input("Input a number(ft) to be converted in meter: "))
result = round(cal(ft),4)
#output
print(f"{ft}ft. in Meter is: {result}")
    