import random

print("———————" * 5  + "\n Welcome to number guessing game \n" + "———————" *5)
print("\n Game info \n1. In this game you have to guess the number from (1 - 50)")
print("2. The chances you will get to guess the number is based on the level of difficulty")
print("3. Also the game will give you hint wheather your guessed number is lower or higher")

print("———————"*5)


def easy():
    print("———————"*5)
    print("\nGreat, You have decided to go with easy level")
    print("Now you have 5 chance use it wisely. Good Luck!!!\n")
    print("The correct number is between (1-50) ")
    guesses = 5
    number = random.randint(1, 50) 
    while guesses > 0:
        try:

            guess = int(input("Enter your guess: "))
            if guess == number:
                print("\nCongralutation, You have won!! ")
                playagain()
                break
            elif guess > 50 or guess < 1:
                print("\nYou have to guess within 1 to 50")
            elif guess < number:
                print("You guessed too low, try getting higher\n")
                guesses -= 1
                print(f"You have {guesses} guesses left")
            elif guess > number:
                print("You guessed too high, try getting lower\n")
                guesses -= 1
                print(f"You have {guesses} guesses left")


            if guesses == 0 and guess !=number:
                print("Game Over, You have lost!! The correct answer was " + str(number))
                playagain()
            
        
        except ValueError:
            print("\nPlease enter number, not string")
     
     

def playagain():
    print("Press 1 to try again \nOr press 2 to exit the game!")
    again = input("What would you like to do: ")
    if again == "1":
        easy()
    elif again == "2":
        print("Thanks for playing the game!!")
    else:
        print("Please enter the correct number!")
        playagain() 



    
def gamemenu():

    print("Please select the difficulty level: ")
    print("1. Easy level (5 chances)")
    print("2. Medium level (3 chances)")
    print("3. difficult levle (1 chance)")

    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            easy()
        else:
            print("PLEASE ENTER CORRECT NUMBER")
            gamemenu()
    except ValueError:
        print("PLEASE ENTER A NUMBER NOT STRINGS\n")
        gamemenu()



gamemenu()



