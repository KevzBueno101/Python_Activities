#Identify if the number is even 
#and higher than 50 or even but lower than 50
#and odd but higher than 50
#or odd but lower than 50

n = float(input("Enter number: "))

if n >= 50:
    if n % 2 == 0:
        print("Even | Higher than 50")
    else:
        print("Odd | Higher than 50")        
elif n <= 50:
    if n % 2 == 0:
        print("Even | Lower than 50")  
    else: 
        print("Odd | Lower than 50")
    