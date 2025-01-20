#import the necessary libraries :
import random 
import datetime

#######################################################################################
#In the beginning I will define a liste in the same file, containning some words
#Then later, I will create a separated text file
words = ['amina', 'aida', 'yannis']

#########################################################################################
#Define the functions :
# This function allows to select randomly an element from the defined list
#I create an empty list and I will fill it with the randomly selected word and its size
def hasard_word() :

    choosen_word = random.choice(words)
    len_word = len(choosen_word)

    return choosen_word, len_word

#########################################################################################
# In this function, I ask the user to fill in the blanks letters, if the letters exists in the selected word, 
# the letter will be appended to the user_word after verification of the emplacement of the letter compared to the selected word
def ask_user(choosen_word, len_word) :
    user_name = input(f"Please, enter your name : ").strip().lower()
    print(f"Hello {user_name}, I have selected randomly a word from the list. It contains {len_word} letters ! ")
    user_word = [' _ ']*len_word #This word is the one the user builds up as they go along
    print(f"{user_word}\n")

    score = 0
    while True :
        user_choice = input(f"Please, select a letter from your choice to fill in the blanks : ").strip()
        if user_choice in choosen_word :  #verify if the letter entered by the user exists in the randomly choosen word
            print('Congratulations, you have found one letter of the word !')
            for i in range (0, len_word) :
                if user_choice == choosen_word[i] : #verify the emplacement of the entered letter compared to the emplacement of the letter in the randomly choosen word
                    user_word[i] = user_choice
            score += 1
                    
        else :
            print(f"Unfound letter")
            score -= 1

        print(user_word)

        # I want to join all the found letters in one string, for this I use the function join(), it is the inverse of split(),
        #it allows to assemble the elements of different sequences like tuples or list (the case here)
        word = ''.join(user_word)
        if ' _ ' not in user_word :
            print(f"Congratulations. You have found the word, it is : {word}")
            break
    return user_word, score, user_name
###########################################################################################
#Here I ask the user if he wants to launch again the game
def play_again() :  
    retry = input(f"Do you want to play again ? (yes/no) :").strip()   
    return retry == 'yes'
       
#############################################################################################
# This function affects the score for each player depending if he finds or not the word
def score_player(user_name, score) :
    if score > 0 :
        print(f"Player n°1 : {user_name} has {score} points")
        
    elif score < 0 :
        print(f"You lost. Good luch for the next time!")

    save_score(user_name, score)
##########################################################################################
# Create 3 function saving, reading ans clearing the data (time, user name and score)
def save_score(user_name, score):
    try:
        current_time = datetime.datetime.now().strftime("%A %d %B %Y à %H:%M:%S")
        history_entry = f"{current_time} - {user_name} : {score}"
        with open("score.txt", "a", encoding="utf-8") as file:
            file.write(history_entry + "\n")
    except Exception as e:
        print(f"An error occurred while saving to history: {e}")

def read_score():
    try:
        with open("score.txt", "r") as file:
            history = file.readlines()
            if not history:
                print("No operations in history.")
            else:
                print("History of operations:")
                for line in history:
                    print(line.strip())
    except FileNotFoundError:
        print("No history file found.")
    except Exception as e:
        print(f"An error occurred while reading history: {e}")

def clear_score():
    try:
        with open("score.txt", "w") as file:
            file.truncate(0)
        print("Score history cleared successfully.")
    except Exception as e:
        print(f"An error occurred while clearing history: {e}")


############################################################################################
#Create the menu
def display_menu(): 
    print(f"\nWelcome to Our hangman game !")
    print(f"\n****** Menu *******")
    print(f"1. Launch the game")
    print(f"2. View score history")
    print(f"3. Clear score history")
    print(f"4. Exit")

#############################################################################################
#The main loop of the game
try:
    while True:
        display_menu()
        choice = input(f"Choose an option (1 - 2 - 3 - 4) :")
        if choice == '1' :
            choosen_word, len_word = hasard_word()
            user_word, score, user_name = ask_user(choosen_word, len_word)
            score_player(user_name, score)
            if not play_again():
                print("Thank you for playing. Come back soon!")
                break
        elif choice == '2' :
            read_score()
            break
        elif choice == '3' :
            while True:  
                confirm = input("Do you really want to clear the score history? (yes/no): ").strip().lower()
                if confirm == "yes":
                    clear_score()
                    break  
                elif confirm == "no":
                    print("The score history not cleared.")
                    break  
                else:
                    print("Invalid input. Please type 'yes' or 'no'.")
                    break

        elif choice == '4' :
            print("\nExiting the game...")
            exit()
except KeyboardInterrupt:
    print("\nExiting the game...")