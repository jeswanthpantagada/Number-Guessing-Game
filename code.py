import os

print("🎮 Multiplayer Number Guessing Game!")
print("Player 1 will set a secret number (1–100). Player 2 will try to guess it.")

# Hide Player 1's input
try:
    import getpass
    secret = getpass.getpass("Player 1, enter a secret number (1–100): ")
    secret_number = int(secret)
except:
    secret_number = int(input("Player 1, enter a secret number (1–100): "))

# Clear screen (optional)
os.system('cls' if os.name == 'nt' else 'clear')

if secret_number < 1 or secret_number > 100:
    print("⚠ Please enter a number between 1 and 100.")
    exit()

attempts = 7
print("\n🔍 Player 2, try to guess the number!")

while attempts > 0:
    try:
        guess = int(input("Your guess: "))
    except ValueError:
        print("⚠ Please enter a valid number.")
        continue

    if guess < 1 or guess > 100:
        print("⚠ Your guess must be between 1 and 100.")
        continue

    if guess == secret_number:
        print("🎉 Correct! You guessed it!")
        break
    elif abs(secret_number - guess) <= 5:
        print("🔥 Close!")
    elif guess < secret_number:
        print("🔼 Too low!")
    else:
        print("🔽 Too high!")

    attempts -= 1
    print(f"Attempts left: {attempts}\n")

if attempts == 0:
    print(f"💀 Game Over! The correct number was {secret_number}.")
