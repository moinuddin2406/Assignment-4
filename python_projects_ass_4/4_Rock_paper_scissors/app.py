import random
print("Welcome to the Rock, paper, scissors game!")

choices = ["rock", "paper", "scissor"]
user_score = computer_score = 0
print("Let's Play!")
while True:
    user_input = input("Type Rock, Paper, Scissor or Q to quit: ").lower()
    if user_input == "q":
        print(f"Final score- you: {user_score}, computer: {computer_score}")
        print("Thanks for playing!")
        break
    if user_input not in choices:
        print("Invalid input, Please try again.")
        continue
    computer_choose = random.choice(choices)
    print(f"Computer choose => {computer_choose}")

    if user_input == computer_choose:
        print("It is a tie!")
    elif (user_input == "rock" and computer_choose =="scissor") or \
            (user_input == "paper" and computer_choose =="rock") or \
            (user_input == "scissor" and computer_choose =="paper")  :
         print("You win!")
         user_score += 1
    else:
        print("Computer win!")
        computer_score += 1
        print(f"Current score- you: {user_score}, computer: {computer_score}")
