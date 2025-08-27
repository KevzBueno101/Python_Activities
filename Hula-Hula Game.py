import random



def intro():
    print(
    """
    |===Welcome to Hula-hula Game!===|
    |===Guess my number from 1-10 ===|
    """)


def play_game():
    secret_number = random.randint(1,10)
    attempts_counter = 0
    while True:
        try:
            print("-------------------")
            user_guess = int(input("Enter your guess: "))
            attempts_counter += 1
            if user_guess == secret_number:
                print(f"\nCongratulations!!\nYou got it in {attempts_counter} attempts")
                option = input("\n1[Main]\n2[Exit]\n").strip().lower()
                if option == "1":
                    return play_game()
                elif option == "2":
                    print("Thank you for playing")
                    break
                else:
                    print("Invalid input")   
                    break
            elif abs(secret_number - user_guess) <= 2:
                print("\nToo close")
            else:
                print("\nTry again")
        except ValueError():
            print("Invalid input.")
intro()
play_game()        
        
        
        
        
        
        
            