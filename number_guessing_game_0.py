import random

#This part is to generate a random number between 1 to 20

computer_think = random.randint(1, 20)
print("I'm thinking a number between 1 and 20")
my_guess = int(input("Take a guess: "))

#This part to compare the guess

if my_guess < computer_think:
    print("It is smaller! I was thinking of", computer_think)
elif my_guess > computer_think:
    print("It is bigger! I was thinking of", computer_think)
else:
    print("Correct! You guessed it right.")

