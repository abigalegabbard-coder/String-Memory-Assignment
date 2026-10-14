import os; import random; import time; import msvcrt; import string

def clear_screen():
    """Clears the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

random_letters_last = 4
random_letters = [random.choice(string.ascii_letters).upper() for _ in range(random_letters_last)]
level_num = 1
display_rand_letters = "".join(random_letters)

def prevent_cheating(): 
    """Remove any pending keystrokes from the keyboard buffer.""" 
    while msvcrt.kbhit(): 
        msvcrt.getwch() 
msvcrt.kbhit() #checks for waiting keystrokes; msvcrt.getwch() removes one. Call the function after clearing the screen and immediately before accepting the player’s guess: 
        
def delay():
    """Provides the delay when displaying the numbers"""
    mystr = ""
    while(mystr == ""):
        mystr = random_letters
    index = 0
    while index < len(mystr):
        print(mystr[index], end="", flush=True)
        time.sleep(1)
        index += 1
# I took this information from a previous assignment, it applies a time(sleep(delay)) to the given variable

def clear_and_create_letters():
    """Creates the random letters, randomizes, and increases the length by 1 each time"""
    global random_letters, display_rand_letters
    random_letters = [random.choice(string.ascii_uppercase)for _ in range(random_letters_last)]
    display_rand_letters = "".join(random_letters)

def display_letters():
    """Display's the random letters each time, and has the delay and level displayed"""
    clear_screen()
    print(f"Level: {level_num}")
    delay()
    time.sleep(5)
    clear_screen()
# This display's the actual random letters, applying a timer to wait 5 sec after all of the letters have been displayed, before moving on

def player_playing_loop():
    global level_num, random_letters_last # This makes it so they can be accessed and changed inside of the function
    while True:
        display_letters()
        player_guess = input("Enter the string you just saw (case insensitive): ").upper()
        if player_guess != display_rand_letters:
            print("Incorrect!")
            print(f"Correct letters: {display_rand_letters}")
            print(f"Your answer: {player_guess}")
            break
        elif player_guess == display_rand_letters:
            print("Correct!")
            level_num+=1
            random_letters_last+=1
            clear_and_create_letters()
# This gathers everything from before, and checks the user's input to see if it is correct, then it repeats, if not correct, it moves on

def display_results():
    """Display's the player's results"""
    if level_num > 1 and level_num <= 2:
        print("Wow, did you understand the game?")
    elif level_num >= 3 and level_num <= 6:
        print("Not bad, keep working at it")
    elif level_num >= 7:
        print("Nice job! You're a memory master!")
    elif level_num == 1:
        print("You succussfully made it through level 0")
# This checks what level it ended on, and then it display's a message based off of what level the user ended on

def playing_again_choice():
    """Asks the user is they would like to play again"""
    global level_num, random_letters_last
    while True:
        player_play_again_choice = input("Would you like to play again? (Y/N): ").strip().lower()
        if player_play_again_choice == "y":
            level_num = 1; random_letters_last = 4
            random_letters.clear()
            clear_and_create_letters()
            player_playing_loop()
            display_results()
        elif player_play_again_choice == "n":
            break
        else:
            print("Enter a y or n next time")
# This asks the user for a 'y' or 'n' and it determines if the game will reset or end

def start_game():
    """Runs through everything"""
    player_start = input("Enter Q to quit, or anything else to start the game: ").lower().strip()
    if player_start == "q":
        return
    else:
        player_playing_loop()
        display_results()
        playing_again_choice()
start_game()