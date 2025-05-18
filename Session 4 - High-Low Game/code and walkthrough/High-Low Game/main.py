import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')
   
    player_score = 0

    for i in range(5):
        
        print("Round number: " + str(i+1))
        # Generate random numbers for player and computer
        computer_num = random.randint(1,100)
        player_num = random.randint(1,100)
        
        # Print the player's number
        print("Your number is: " + str(player_num))

        # Initialize 
        player_wins_the_round = False
        
        while True: 
            # Get input from the player
            player_guess = input("Enter your guess: ")
            # player wrote "HIGHER"
            player_guess = player_guess.lower()

            if player_guess == "higher" or player_guess == "lower":
                break
            else: 
              print("Enter a valid input: ")

        # Conditions 
        if player_guess == "higher" and player_num > computer_num:
            player_wins_the_round = True
            player_score += 1    
        elif player_guess == "lower" and player_num < computer_num:
            player_wins_the_round = True
            player_score += 1    
        
        if player_wins_the_round: 
            print("You were right! The computer's number was " + str(computer_num))
            print("Your score is " + str(player_score))
        else:
            print("Your guess is incorrect! The computer's number was " + str(computer_num))
            print("Your score is " + str(player_score))
    
    print("Thanks for playing!")

    if player_score == NUM_ROUNDS:
        print("Congratulations for the perfect game! ")
    elif player_score >= NUM_ROUNDS//2:
        print("Good job!")
    else:
        print("Better luck next time")



if __name__ == "__main__":
    main()