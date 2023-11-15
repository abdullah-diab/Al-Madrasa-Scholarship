import random

user = input("What is your choice? ")
pc = random.choice(["rock", "paper", "scissors"])

print(f"User chose: {user}")
print(f"PC chose: {pc}")

if user == pc:
  print("It's a tie!")
elif user == "rock" and pc == "scissors":
  print("You win!")
elif user == "paper" and pc == "rock":
  print("You win!")
elif user == "scissors" and pc == "paper":
  print("You win!")
else:
  print("You lose!")