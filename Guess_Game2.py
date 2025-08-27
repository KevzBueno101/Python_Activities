# Guess Game

secret_number = 17

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

while True:
    user_guess = int(input("\nEnter your guess: "))
    if user_guess == secret_number:
        print("\nBINGO!")
        break
    elif abs(secret_number - user_guess) <= 2:
        print("\nYou're too close!")
    else:
        print("\nUh oh! Try again.")
        