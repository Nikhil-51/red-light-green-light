import time
import random

def play_game():
    # Score tracking (global variables for wins and losses)
    global wins, losses
    
    # Select difficulty
    print("\nSelect difficulty:")
    print("1. Easy (20 meters, 40 seconds)")
    print("2. Medium (30 meters, 30 seconds)")
    print("3. Hard (40 meters, 25 seconds)")
    difficulty = input("Enter 1, 2, or 3: ").strip()
    
    if difficulty == "1":
        safe_distance, game_duration = 20, 40
    elif difficulty == "2":
        safe_distance, game_duration = 30, 30
    elif difficulty == "3":
        safe_distance, game_duration = 40, 25
    else:
        print("Invalid choice. Defaulting to Medium difficulty.")
        safe_distance, game_duration = 30, 30

    # Game settings
    player_distance = 0  # starting distance
    player_alive = True

    # Introduction
    print("\nWelcome to the Squid Game: Red Light, Green Light!")
    print("Rules:")
    print(f"1. Reach the safe zone ({safe_distance} meters) within {game_duration} seconds.")
    print("2. Move only during 'Green Light'.")
    print("3. If you move during 'Red Light', you're eliminated.")
    print("4. For 'yes' press 'y' and for 'no' press 'n'")
    print("5. Good luck!\n")

    # Timer setup
    start_time = time.time() #it starts the timer

    while player_alive and player_distance < safe_distance:
        light = random.choice(["Red Light", "Green Light"])  # Random light selection
        print(f"{light}!")
        
        move = "" 
        while move not in ["y", "n"]: #you can only choose y and n, y for yes and n for no
            move = input("Do you want to move? (yes/no): ").strip().lower() #this removes spaces and converts the string into lowercase if needed
        
        if light == "Green Light" and move == "y":
            # Randomly chooses steps between 1 to 5
            step = random.randint(1, 5)
            print(f"Step size chosen: {step}")

            player_distance += step #all distance is added in this variable
            print(f"You moved forward {step} meters. Total distance: {player_distance} meters.")
        elif light == "Red Light" and move == "y":
            print("You moved during 'Red Light'! You're eliminated.")
            player_alive = False
        elif move == "n":
            print("You chose to stay still.")

        # Check if time is up
        elapsed_time = time.time() - start_time
        if elapsed_time >= game_duration:
            print("\nTime's up! You didn't reach the safe zone.")
            player_alive = False
            break

        # Display time remaining and distance left
        time_left = game_duration - elapsed_time
        print(f"Time remaining: {round(time_left, 2)} seconds.")
        print(f"Distance to safe zone: {safe_distance - player_distance} meters.\n")

    # Game result
    if player_alive and player_distance >= safe_distance:
        print("\n🎉 Congratulations! You reached the safe zone and won the game!")
        wins += 1
    elif player_alive:
        print("\nYou survived but failed to reach the safe zone.")
        losses += 1
    else:
        print("\nGame Over! Better luck next time.")
        losses += 1

# Main program
wins, losses = 0, 0  # Initialize score tracking
while True:
    play_game()
    print(f"\nCurrent Score: {wins} Wins, {losses} Losses")
    
    replay = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if replay != "y":  # If the user does not press "y", exit the loop
        print("Thanks for playing! Goodbye!")
        break