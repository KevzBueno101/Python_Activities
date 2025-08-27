
power = 1

base = int(input("Enter base: "))
for expo in range(10):
    print(f"{base} to the power of {expo} is {power}") 
    power *= base 