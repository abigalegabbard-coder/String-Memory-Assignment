import os
import random
import time
import msvcrt
import string

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

random_letters_last = 4
random_letters = [random.choice(string.ascii_letters).upper() for _ in range(random_letters_last)]
level_num = 1

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
    clear_screen()
    while index < len(mystr):
        print(mystr[index], end="", flush=True)
        time.sleep(.5)
        index += 1

def player_playing_loop():
    while True:
        print(f"Level: {level_num}")
        delay()
        clear_screen()
        prevent_cheating()
        player_guess = input("Enter a guess of what the letter's were: ").upper()
        if player_guess != random_letters:
            print("Incorrect!")
            print(f"Correct string: {random_letters}")
            print(f"Your answer: {player_guess}")
            break
        elif player_guess == random_letters:
            print("Correct!")
            level_num+1
            random_letters_last+1
        elif player_guess == "q" or player_guess == "Q":
            print("Thanks for playing")
            quit
player_playing_loop()

def display_results():
    print(f"The level you got to: {level_num}")
    if level_num > 1 and level_num <= 2:
        print("Wow, did you understand the game?")
    elif level_num >= 3 and level_num <= 6:
        print("Not bad, keep working at it")
    elif level_num >= 7:
        print("Nice job! You're a memory master!")
    elif level_num == 1:
        print("You succussfully made it through level 0")
display_results()

def playing_again_choice():
    while True:
        player_play_again_choice = input("Would you like to play again? (Y/N): ").strip().lower()
        if player_play_again_choice == "y":
            level_num = 1
            random_letters_last = 4
            player_playing_loop()
            display_results()
        elif player_play_again_choice == "n":
            print("Thank you for playing")
            break
        else:
            print("Enter a y or n next time")
playing_again_choice()