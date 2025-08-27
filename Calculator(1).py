import time

def plus(x,y):
    z=x+y
    print(f"{x} + {y} = {z}")
def minus(x,y):
    z=x-y
    print(f"{x} - {y} = {z}")
def mult(x,y):
    z=x*y
    print(f"{x} * {y} = {z}")
def div(x,y):
    z=x/y
    print(f"{x} + {y} = {z}")
def display():
    print("----------------")    

while True:
    u = int(input(
        """
        __________________
        Choose an operator
        1. Add(+)
        2. Minus(-)
        3. Multiply(*)
        4. Divide(/)
        5. Exit
        __________________
        """))
    if u == 5:
        print("Exiting calculator.")
        time.sleep(2)
        print("Byeee")
        break
        
    x = float(input("Enter a number: "))
    y = float(input("Enter another number: "))
    print("\n")
    if y == 0:
        print("Division by zero is not allowed")
        continue 
    if u == 1:
        display()
        plus(x,y)
        display()
    elif u == 2:
        display()
        minus(x,y)
        display()
    elif u == 3:
        display()
        mult(x,y)
        display()
    elif u == 4:
        display
        div(x,y)
        display()
    else:
        print("Invalid Input")
                    
            

        
        
    
    
            