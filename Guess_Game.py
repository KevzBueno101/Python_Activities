# Guess Game

secret_number = 777

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
    user_guess = int(input("Enter your guess: "))
    if user_guess == secret_number:
        print("Well done, muggle! You are right.")
        break
    else:
        print("Uh oh! Try again.")