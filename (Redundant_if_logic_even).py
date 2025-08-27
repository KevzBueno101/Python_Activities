#Identify if the number is even 
#and higher than 50 or even but lower than 50
#and odd but higher than 50
#or odd but lower than 50

n = int(input("Enter number: "))

if n % 2 == 0 and n >=50:
    print("Even and Higher than 50")
elif n % 2 == 0 and n <= 50:
    print("Even and Higher than 50")
elif n % 2 != 0 and n >= 50:       
    print("Odd but lower than 50")
elif n % 2 != 0 and n <= 50:
    print("Odd but ")    
     
    