import random

min_attempts = float('inf')

while True:
    print("Welcome to the guessing game! Please pick a number between 1 and 10.")
    player_choice = int(input())
    pc_choice = random.randint(1, 10)
    attempts = 1

    while player_choice != pc_choice:
        if player_choice < pc_choice:
            print("Too low, try again.")
        else:
            print("Too high, try again.")
        player_choice = int(input())
        attempts += 1

    if attempts < min_attempts:
        min_attempts = attempts

    print("Congratulations! You have guessed the number in", attempts, "attempts.")
    print("The minimum number of attempts so far is", min_attempts)
    play_again = input("Do you want to play again? (yes/no)")
    if play_again.lower() == "no":
        break
