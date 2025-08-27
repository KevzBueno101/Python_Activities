import random

secret_number = random.randint(1,10)

print(
    """
    |===Welcome to Hula-hula Game!===|
    |===Guess my number from 1-10 ===|
    """)

while True:
    try:
        print("-------------------")
        user_guess = int(input("\nEnter your guess: "))
        
        if user_guess == secret_number:
            print("\nBINGO!")
            break
        elif abs(secret_number - user_guess) <= 2:
            print("\nToo close")
        else:
            print("\nTry again")
    except ValueError():
        print("Invalid input.")
        
        
        
            