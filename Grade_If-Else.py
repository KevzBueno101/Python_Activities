grade = int(input("Enter the grade: "))

if grade >= 90 and grade <= 100:
    print("Grade: A")
elif grade >= 75 and grade <= 89:
    print("Grade: B") 
elif grade >= 60 and grade <= 74:
    print("Grade: C")
elif grade >= 50 and grade <= 59:
    print("Grade: D")
elif grade < 50:
    print ("Grade: F")  

if grade < 50:
    print("FAILED")
else:
    print("PASSED")        