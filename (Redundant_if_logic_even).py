#Identify if the number is even 
#and higher than 50 or even but lower than 50
#and odd but higher than 50
#or odd but lower than 50

n = int(input("Enter number: "))

if n % 2 == 0:
    if n >= 50:
        print("Even and higher than 50")
    else:
        print("Even and lower than 50")
else:
    if n >= 50:
        print("Odd and higher than 50")
    else:
        print("Odd and lower than 50")
    
