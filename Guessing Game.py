import random

"""This function generates a random number between 0 and 10 and allows the user to guess it.

The user has 3 tries to guess the correct number. If the user guesses the correct number, the function prints "You Win!". Otherwise, the function prints "Wrong!" and the number of tries remaining.
"""

try_times = 3
z = 0
guess = random.randint(0, 10)
while try_times > 0:
    try:
        correct_num = int(input("Enter Corrct Number: "))
    except ValueError:
        print("Please enter a numeric value.")
        continue  # This will skip the rest of the code in this iteration of the loop and go back to the top

    try_times -= 1
    if (try_times == 0):
        print(f"You lose Because Your Times is {try_times}")
        print(f"The Correct Number Was {guess}")
    elif (correct_num == guess):
        print("You Win!")
        break
    elif (correct_num > guess):
        print("Too High!")

    elif (correct_num < guess):
        print("Too Low!")
