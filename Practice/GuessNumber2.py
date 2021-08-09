import random
print("Guessing number - Python")
# Define the range of numbers we have to consider when generating random number (top_secret)
minNumber = 1
maxNumber = 10
user_guesses = 0
# The total amount of guesses 
total_guesses = []
# Define maximum number of guesses
max_guesses = 4
# Rules and Information/Instructions
print("~~~~~~RULES~~~~~~")
print("You only have {} attempts!".format(max_guesses))
print("~~~~~~INSTRUCTIONS~~~~~~")
print("Guess a number between {} and {} ".format(minNumber, maxNumber ))
# Generate a random secret number - Automatically
top_secret = random.randint(minNumber, maxNumber)

while user_guesses < max_guesses:
    attempts_left = max_guesses - user_guesses
    # Print information about the number of attempts left
    print("You have {} attempts left. ".format(attempts_left))
    guess = int(input("Guess a number: "))
    # Update the number of guesses the user has taken
    user_guesses += 1
    # Save the number entered by the user
    total_guesses.append(guess)
    
    # Let's add some if statements in order to inform the user about each guess he/she has taken (Too low | Too high)
    if guess < top_secret:
     print("Too low. Try again!")
     continue
    elif guess > top_secret:
     print("Too high. Try again!")
     continue
    elif guess == top_secret:
      print("You rock! WIN!")
      # If the user wins, we have to inform about the number of guesses taken and print out these guesses. 
      print("You have taken {} guesses".format(user_guesses))
      print("Summary of your guesses: {}".format(total_guesses))
      break
    
else:
    print("Game over!!!")
    print("Final stats:")
    # If the user is defeated, we also have to inform about the number of guesses taken and print out these guesses. 
    print("You have taken {} guesses".format(user_guesses))
    print("Summary of your guesses: {}".format(total_guesses))