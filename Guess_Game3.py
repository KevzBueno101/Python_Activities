import random

secret_number = random.randint(1,100)

print(
    """
    Welcome To Guess The 
    Secret Number Game!!
    """
    )
while True:
  try:
    user_guess = int(input("Enter your guess: "))
    if user_guess == secret_number:
        print("BINGO!!")
        break
    elif abs(secret_number - user_guess) <= 5: 
            print("You're too close.")
    elif abs(secret_number - user_guess) <= 10:
            print("You're close to right one!") 
    else:
        print("Uh oh! Try again.")       
  except ValueError:
      print(
          """×Invalid input×
       Must be an integer number.""")
            
        