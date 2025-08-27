def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1

    product = 1
    for i in range(2, n + 1):
        product *= i
    return product

u = int(input("Enter a number: "))

for n in range(1, u + 1):  # testing
    print(f"{n}! = {factorial_function(n)}")

