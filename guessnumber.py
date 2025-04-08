import random

secret_number = random.randint(1, 20)
attempts = 0

print("🎮 Welcome to 'Guess Game!'")
print("I am thinking of a number between 1 and 20.")
print(f"You have {attempts} attempts. Good luck\n")

while attempts > 0:
    guess = int(input("Enter your guess: "))
    if guess == secret_number:
        print("Congrats! You guessed it right")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

    attempts -= 1
    print(f"You have {attempts} attempts left.")

    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The number was {secret_number}.")