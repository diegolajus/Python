  
"""
    Guessing number - Python - Truzz Blogg
    
    Original video (Truzz Blogg Channel): https://youtu.be/AoSExJn9zlA
    
    Simple guessing game where the user has 4 attempts to find out
    the number we are looking for.
"""
# Print some information about the game
print("Guessing number - Python - Rules: You only have 4 attempts!")
# Define the secret number (in this version, we are doing this task manually)
top_secret = 7
# Count the number of guesses
user_guesses = 0
# Define maximum number of guesses
max_guesses = 4

# Let's try to find the correct guess - While Loop
while user_guesses < max_guesses:
    attempts_left = max_guesses - user_guesses
    print("You have {} attempts left. ".format(attempts_left))
    guess = int(input("Guess a number: "))
    user_guesses += 1
    if guess == top_secret:
        print("You rock! WIN!")
        break
    else:
        print("So sorry! Keep trying!")

# When your while Loop condition does not match, we are going to go through the 'else' option - Game Over!
# else:
    # print("Game over!!!")