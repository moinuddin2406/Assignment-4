import random
print("Welcome to the Number Guessing Game")

low = 1
high = 10

print("Think a number between 1 to 10 and computer will be guess it.")
if low <= high:
    guess = random.randint(low, high)
    print("Computer guess is: " , guess)
    while True:
        feedback = input("Is the guess too high (H) too low (L) or correct (C) ?").strip().upper()
        if feedback == "C":
           print("The computer guessed your number correctly. ")
           break
        elif feedback == "H":
            high = guess-1
            guess = random.randint(low,high)
            print("Computer guess is: " , guess)
        elif feedback == "L":
            low = guess+1
            guess = random.randint(low,high)
            print("Computer guess is: " , guess)
        else:
            print("Invalid input. Please enter C,H or L.")
    if low > high:
        print("The number is not in the range.Plase try again.")
     

       