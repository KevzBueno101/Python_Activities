#identifies if a:
# infant, toddler, teen, 
#young adult, adult, senior citizens

age = int(input("Enter your age: "))

if age <= 1:
    print("Infant")
elif age <= 3:
    print("Toddler")   
elif age <= 12:
    print("Child") 
elif age <= 19:
    print("Teen/Adolescent")        
elif age <= 39:
    print("Young adult")    
elif get <= 59:
    print("Adult")  
else:
    print("Senior")      