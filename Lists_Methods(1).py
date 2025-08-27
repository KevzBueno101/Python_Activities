mylist = [5,4,3,2,1]#laog ning listahan mo

def divider():
    print("------------------------------------")


while True:
    print("------------------------------------")
    print(f"Your list: {mylist}")
    print("------------------------------------")
    a = int(input("""
    --------------
    Please Choose:
    1. Append
    2. Sort
    3. Insert
    4. Remove
    5. Pop
    6. Index
    7. Count
    8. Print
    9. Exit
    -------------
    """)) #pilian Ning methods kung ano gigibuhon sa mga nakalista
    divider()
    if a==1:
        x = int(input("Enter elements you want to append: "))
        mylist.append(x)
        print(mylist)
    elif a==2:
        mylist.sort()
        print(mylist)
    elif a==3:
        x = int(input("Enter elements you want to insert: "))
        y = int(input("To where it will be inserted? "))
        mylist.insert(y,x)
        print(mylist)
    elif a==4:
        x = int(input("Enter elements you want to remove: "))
        mylist.remove(x)
        print(mylist)
    elif a==5:
        x = int(input("Enter the index you want to pop: "))
        mylist.pop(x)
        print(mylist)
    elif a==6:
        x = int(input("Enter elements you want to find its index: "))
        print(mylist.index(x))
    elif a==7:
        x = int(input("Enter elements you want to count: "))    
        print(mylist.count(x))
    elif a==8:
        print(mylist)    
    elif a==9:
        break
    else:
        print("Invalid input. Please choose between 1-9")

            