# A guess game
import random
# I set the game ending to false, so i begin with true
game_running = True

while game_running:
    # Greeting my player
    print("I'm thinking of a number between 1 and 10, Can you guess?")
    # Let the system generate the number using int
    secret_num = random.randint(0, 20)
    # Let the system generate the number using range
    # 8secret_num = random.randrange(0, 20, 2)
    # Set the player's number outside the range; this is used becuz as long as the guess_num is not equal to secret_num, the player can keep playing
    #guess_num = -1
    guess = False
    # Loop until the player guesses our number
    while guess == False:
   # while guess_num != secret_num:
        # Get the players guess number
        guess = input("please enter a number: ")
        # Does the user want to quit
        if guess == "quit":
            game_running = False
            break
        # Otherwise when player wants to continue
        else:
            # Convert user input to integer
            guess_num = int(guess)
        # The player guess the program's right number
        if guess_num == secret_num:
            print("Congratulations!!")
            # Otherwise try again
        else:
            print ("Try again")
# Say goodbye to the player
# Good project
# Thanks for making it open source
print("Bye!!")

