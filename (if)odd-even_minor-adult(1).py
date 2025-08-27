#Identify if the number is even 
#and higher than 50 or even but lower than 50
#and odd but higher than 50
#or odd but lower than 50

n = float(input("Enter number: "))

if n % 2 == 0:
    if n > 18:
        print("Even number | Adult")
    else:
        print("Even number | Minor")  
else:
    if n > 18:
        print("Odd number | Adult")
    else:
        print("Odd number | Minor")