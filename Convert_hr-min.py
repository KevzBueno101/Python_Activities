#Conversion of hours to minutes

def conv(hr):
    return hr * 60

hr = int(input("Enter hour: "))
hrs_min = conv(hr)

print(f"{hr} hr is {hrs_min} min")