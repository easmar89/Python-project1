import random

def greetings(name):
    welcome_message = "HELLO {} AND WELCOME TO THE CORONA BOREDOM KILLER GAME".format(name.upper())
    print("*" * len(welcome_message))
    print(welcome_message)
    print("*" * len(welcome_message))

high_score = float('inf')

def start_game(n):
    answer = random.randint(1,100)
    number_of_guesses = 1
    
    while True: 
        
        try:
            guess = int(input("Guess the number between 1 and 100: "))
        except ValueError:
            print("Please enter a digit between 1 and 100")
            continue
        if guess < 1 or guess > 100:
            print("Invalid guess, try again:")
            continue  

        if guess < answer:
            print("The correct number is higher")
            number_of_guesses += 1
        elif guess > answer: 
            print("The correct number is lower")
            number_of_guesses += 1
        else: 
            print("YES! Congratulations!!!")
            print("Number of attempts is: ", number_of_guesses, " attepmt(s)")
            if n > number_of_guesses:
                return number_of_guesses
            else: 
                return n
            break        

player_name = input("Please enter your name: ")
greetings(player_name)

high_score = start_game(high_score)


while True: 
    print("High score is: ", high_score)
    play_again = str(input("would you like to play again? Y/N: "))
    if play_again == "Y".lower():
        high_score = start_game(high_score)
    else:
        print("GOODBYE!! see you next time! :) ")
        break


