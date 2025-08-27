
def bmi(weight, height):#define BMI formula
    return weight / height**2
def bmi_class(bmi_result):#define BMI class
    if bmi_result < 18: 
        return "Underweight"
    elif 18.5 <= bmi_result < 25:
        return "Normal"
    elif 25.5 <= bmi_result < 30:
        return "Overweight"
    else:
        return "Obese"
#user input
weight = float(input("Weight(kg): "))
height = float(input("Height(m): "))
#bmi calculator
bmi_result = bmi(weight, height)
#bmi classification 
category = bmi_class(bmi_result)

##Output##
print(f"Your BMI is: {bmi_result: .1f}")
print(f"Category: {category}")

        
          